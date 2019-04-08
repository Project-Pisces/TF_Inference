
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import time
import shutil, os
import time
import datetime
import numpy as np
import tensorflow as tf
import smtplib

"""
Reads .pb file included on the 
tf_files directory
"""
def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

def read_tensor_from_image_file(file_name, input_height=299, input_width=299, input_mean=0, input_std=255):
  input_name = "file_reader"
  output_name = "normalized"
  file_reader = tf.read_file(file_name, input_name)
  if(file_name.endswith(".jpg")):
    image_reader = tf.image.decode_jpeg(file_reader, channels = 3,
                                        name='jpeg_reader')
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0)
  resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.Session()
  result = sess.run(normalized)

  return result

def load_labels(label_file):
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label

"""
This function is meant to send out an email when we find a chinook
as of now, it is only sending text; however, it is possible to send images
in the form of a JSON file due to the limited networking at the river.
"""
#name = project
#lastname = pisces
#projectpiscesrover@gmail.com
#bday = 03/31/1920
#pwd = salmonxtrout
def notify_user():
  user = 'projectpiscesrover@gmail.com'
  pwd = 'salmonxtrout'
  recipient = 'edward.melendez@sjsu.edu'
  subject = 'Good News from Pisces ROV'
  body = """If you are getting this email it means that christian was able to train the ML model to find a chinook then sent you an email about it"""

  FROM = user
  TO = recipient if isinstance(recipient, list) else [recipient]
  SUBJECT = subject
  TEXT = body

  # Prepare actual message
  message = """From: %s\nTo: %s\nSubject: %s\n\n%s
  """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
  try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.ehlo()
      server.starttls()
      server.login(user, pwd)
      server.sendmail(FROM, TO, message)
      server.close()
      print('successfully sent the mail')
  except:
      print('failed to send mail')

if __name__ == "__main__":
  input_height = 224
  input_width = 224
  input_mean = 128
  input_std = 128
  input_layer = "input"
  output_layer = "final_result"

  parser = argparse.ArgumentParser()
  parser.add_argument("--image")
  parser.add_argument("--graph")
  parser.add_argument("--labels")
  args = parser.parse_args()

  if args.graph:
    model_file = args.graph

  if args.labels:
    label_file = args.labels

  graph = load_graph(model_file)

  # loop to get the length and verify it is > 0, keep looping
  # while(os.listdir("/tmp/opencv_frame/"))
  # At beginning, get all filenames in directory, then loop filenames
  
  # Make into an outiside loop chekcing for length

  print(len(os.listdir("/tmp/opencv_frame/")))

  while(len(os.listdir("/tmp/opencv_frame/")) > 0):
    print("Waiting for images to load...")
    time.sleep(12)
    print(len(os.listdir("/tmp/opencv_frame/")), "items in the snapshot folder")
    for file_name in os.listdir("/tmp/opencv_frame/"):
      full_image_path = "/tmp/opencv_frame/" + file_name
      
      if file_name.endswith("jpg"):
        print(full_image_path)
        print('_________________')
        t = read_tensor_from_image_file(full_image_path,
                                        input_height=input_height,
                                        input_width=input_width,
                                        input_mean=input_mean,
                                        input_std=input_std)

        input_name = "import/" + input_layer
        output_name = "import/" + output_layer
        input_operation = graph.get_operation_by_name(input_name)
        output_operation = graph.get_operation_by_name(output_name)

        labels = load_labels(label_file)

        with tf.Session(graph=graph) as sess:
          
          start = time.time()
          results = sess.run(output_operation.outputs[0], {input_operation.outputs[0]: t})

          end=time.time()
        print('\nEvaluation time (1-image): {:.3f}s\n'.format(end-start))

        results = np.squeeze(results)
        top_k = results.argsort()[-1:][::-1]

        if(labels[top_k[0]] == 'chinook' and (results[top_k[0]] > .5)):
          print('OMG, its a Chinook!')
          print('I am', results[top_k[0]], 'confident about this')
          ts = time.time()
          st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
          shutil.copy(full_image_path, '/tmp/found_endagered_fish/' + st + '.jpg')
          notify_user()
          os.remove(full_image_path)

        elif(labels[top_k[0]] == 'chinook' and (results[top_k[0]] < .5) and (results[top_k[0]] > .4)):
          print('Could be a Chinook!')
          print('I am', results[top_k[0]], 'confident about this')
          ts = time.time()
          st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        elif(labels[top_k[0]] == ('black_crappie' or 'bluegill' 
                                  or 'pacific_lamprey' or 'riffle_sculpin'
                                  or 'brown_bullhead' or 'redear_sunfish'
                                  or 'large_mouth_bass' or 'golden_sinner'
                                  or 'common_carp' or 'channel_catfish')
                                  and (results[top_k[0]] > .5)):
          print('Found a fish but not the target' + '\n' + labels[top_k[0]])
          print('I am', results[top_k[0]], 'confident about this')
          ts = time.time()
          st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
          shutil.copy(full_image_path, '/tmp/basic_fish/' + st + '.jpg')
          os.remove(full_image_path)

        else:
          print('Scanned image but found nothing of interest')
          print('I am', results[top_k[0]], 'confident about this')
          os.remove(full_image_path)
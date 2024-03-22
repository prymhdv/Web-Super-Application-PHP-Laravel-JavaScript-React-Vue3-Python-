import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print (str(smallestID) + "-" + json.dumps(distance))
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print (str(smallestID) + "-" + json.dumps(distance))
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print (str(smallestID) + "-" + json.dumps(distance))
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print (str(smallestID) + "-" + json.dumps(distance))
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print (str(smallestID) + "-" + json.dumps(distance))
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print (str(smallestID) + "-" + json.dumps(distance))
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print (str(smallestID) + "-" + json.dumps(distance))
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
v
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
import cv2
import sys
import json
from matplotlib import pyplot as plt

arrayString = sys.argv[1].split(",")

final = []

for i in range(len(arrayString)):
    final.append(arrayString[i].split("-"))

img1 = cv2.imread(final[0][1], 0)

for i in range(1, len(arrayString)):

    img2 = cv2.imread(final[i][1], 0)

    # Initiate STAR detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

    if i == 1:
       distance = matches[0].distance
    else:
       if distance > matches[0].distance:
           distance = matches[0].distance
           smallestID = final[i][0]

print str(smallestID) + "-" + json.dumps(distance)
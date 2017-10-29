<!-- .slide: class="center" -->
# Intel Delta8 practice

<!----------------------------------------------------------------------------->

---
## Day 1
### Agenda
* Divide into teams
* Intel Galileo sample
* What will we make?

<!----------------------------------------------------------------------------->

---
<!-- .slide: class="center" -->
### Intel Galileo sample: Canny edge detector

<!----------------------------------------------------------------------------->

---?code=src/canny.ino&lang=cpp

#### Arduino sketch

@[1-6]
@[8-10]

<!----------------------------------------------------------------------------->

---?code=src/canny_board.py&lang=python

#### Device (server)

@[1-6]
@[8-14]
@[16-21]
@[23-28]
@[30-33]
@[36-43]

```bash
$ scp src/canny_board.py root@x.x.x.x:/home/root
$ ssh root@x.x.x.x
root@x.x.x.x:~$ python canny_board.py
```

@[-]

<!----------------------------------------------------------------------------->

---?code=src/canny.py&lang=python

#### Host (client)

@[1-10]
@[12-12]
@[14-33]
@[36-36]
@[38-41]
@[42-46]
@[48-50]
@[52-56]

```bash
$ python src/canny.py -i x.x.x.x
```

@[-]

<!----------------------------------------------------------------------------->

---?image=images/canny.png&size=auto 90%

<!----------------------------------------------------------------------------->

---
### Available deep learning models
* (FD) Face detection
* (ER) Emotions recognition
* (ID) Face recognition
* (GAN) Face generation

<!----------------------------------------------------------------------------->

---
### Homework
* 5-min team
* Download and install Android Studio

---

## Day 2

---

### Authorize device

```shell
$ lsusb
Bus 003 Device 067: ID 1bbb:f017 T & A Mobile Phones Alcatel One Touch L100V / Telekom Speedstick LTE II

$ echo SUBSYSTEM==\"usb\", \
>      ATTRS{idVendor}==\"1bbb\", \
>      ATTRS{idProduct}==\"f017\", \
>      MODE==\"0666\" >> /etc/udev/rules.d/51-android.rules

$ sudo adb kill-server && sudo adb start-server && sudo adb devices
List of devices attached
PEJB25BF4MXAHN4	device
```

---

### Face detector

|               |                                                              |
|---------------|--------------------------------------------------------------|
| Input         | any size BGR image                                           |
| Preprocessing | subtract mean:<br> `B - 104, G - 177, R - 123`               |
| Output        | Blob of bounding boxes with size `1x1xNx7`<br> where `N` - number of detections<br> and an every BBox is a vector<br>`id, classId, confidence, left, top, right, bottom` |

---

### Fast-neural-style

|               |                                                              |
|---------------|--------------------------------------------------------------|
| Input         | any size BGR image                                           |
| Preprocessing | subtract mean:<br>`B - 103.939, G - 116.779, R - 123.68`     |
| Output        | Stylized planar BGR image                                    |
| Postproc.     | add mean:<br>`B + 103.939, G + 116.779, R + 123.68`<br>clip to [0, 255] |

---

### BEGAN, faces generator

|               |                                                              |
|---------------|--------------------------------------------------------------|
| Input         | `1x64` uniform `[-1, 1]` noise                               |
| Output        | Planar BGR image                                             |

---

### Emotion recognition

|               |                                                              |
|---------------|--------------------------------------------------------------|
| Input         | `48x48` grayscale face image                                 |
| Output        | `1x10` vector of emotions "probabilities"                    |

---

---

### Create Android project: style transfer

---?image=images/1_start_new_project.png&size=auto 90%

---

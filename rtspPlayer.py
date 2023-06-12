import cv2, sys, os

cap = cv2.VideoCapture()
cap.setExceptionMode(True)


ip = None
user = None
password = None
port = 554
stream = None
size = 1

exitFlag = False

arguments = sys.argv[1:]
options = "hmo:"
long_options = ["help", "ip", "user", "password", "port", "stream"]
if len(arguments) == 0:
    arguments.append('-h')

try:

    for index in range(len(arguments)):
        arg = arguments[index]
        if(index < len(arguments) - 1):
            val = arguments[index+1]
        if arg in ("-h", "--help"):
            print("\nCommand line options:\n")
            print("\t-h --help\tDisplay help\n")
            print("\tRequired options:\n")
            print("\t\t-i --ip\t\tSet rtsp stream IP")
            print("\t\t-u --user\tSet rtsp stream user")
            print("\t\t-p --password\tSet rtsp stream password")
            print("\t\t-s --stream\tSet rtsp stream endpoint\n")
            print("\n\tAdvanced options:\n")
            print("\t\t--port\t\tSet rtsp stream port, default: 554")
            print("\t\t--size\t\tSet stream resolution scale percentage, default: 100")
            print("\nPass arguments to build rtsp url:\n'rtsp://{user}:{password}@{ip}:{port}/{stream}'\n")
            print("Press any key to continue...")
            input()
            sys.exit()
        elif arg in ("-i", "--ip"):
            ip = val
        elif arg in ("-u", "--user"):
            user = val
        elif arg in ("-p", "--password"):
            password = val
        elif arg in ("-s", "--stream"):
            stream = val
        elif arg == "--port":
            port = val
        elif arg == "--size":
            for char in val:
                if not char.isdigit:
                    print("Size must be a number\n")
                    print("Press any key to continue...")
                    input()
                    sys.exit()
            size = int(val)/100

except Exception as e:
    print(f"{e}\n")
    print("Press any key to continue...")
    input()
    sys.exit()

if not ip:
    print('IP address is required')
    exitFlag = True
if not user:
    print('User is required')
    exitFlag = True
if not password:
    print('Password is required')
    exitFlag = True
if not stream:
    print('Stream is required')
    exitFlag = True

if exitFlag:
    print("\nPress any key to continue...")
    input()
    sys.exit()

rtspUrl = f"rtsp://{user}:{password}@{ip}:{port}/{stream}"

print(f"Connecting to {rtspUrl}")

vid = cv2.VideoCapture(rtspUrl)
ret, frame = vid.read()

if not ret:
    print(f"Failed to connect to {rtspUrl}")
    print("Press any key to continue...")
    input()
    sys.exit()

frame = cv2.resize(frame, (round(size * frame.shape[0]),round(size * frame.shape[1])), interpolation=cv2.INTER_CUBIC)
cv2.imshow(f"{ip}", frame)

while(vid.isOpened()):
    key = cv2.waitKey(27) & 0xFF
    if key == 27:    
        break
    try:
        cv2.getWindowProperty(f"{ip}",1)
    except:
        break
    ret, frame = vid.read()
    frame = cv2.resize(frame, (round(size * frame.shape[1]),round(size * frame.shape[0])), interpolation=cv2.INTER_CUBIC)
    cv2.imshow(f"{ip}", frame)

vid.release()
cv2.destroyAllWindows()

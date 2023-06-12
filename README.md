# rtspPlayer

Stream rtsp video

Requires IP, user, password, and endpoint to be passed as command line arguments

Command line options:

        -h --help       Display help

        Required options:

                -i --ip         Set rtsp stream IP
                -u --user       Set rtsp stream user
                -p --password   Set rtsp stream password
                -s --stream     Set rtsp stream endpoint


        Advanced options:

                --port          Set rtsp stream port, default: 554
                --size          Set stream resolution scale percentage, default: 100

Pass arguments to build rtsp url:
'rtsp://{user}:{password}@{ip}:{port}/{stream}'

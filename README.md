# chat-room
Chat Room hosted by "server.py" scrpit and connected via "client.py" scrpit

## Running
Run "server.py" on device you would like the server to run on.

Run "client.py" on device you are connecting from. Ensure you change "SERVER" to the ip address the server is running on.

## Notes:
Currently set up for local networks. Can be extended via port forwarding.

To set up creds.txt file:
     * "send_address" is the gmail address to send from
     * "password_for_send_address" is the password for the gmail account (I recommend setting up an app password for security)
     * "recieve_address" is the email address that you would like the notifications to be sent to

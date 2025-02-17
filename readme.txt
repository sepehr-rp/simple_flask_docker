

###############################

Structure:

	web_app
	|
	|==> static 
	|	|
	|	|==> styles
	|		|
	|		|==> index.css
	|	
	|
	|==> templates
	|	|
	|	|==> index.html
	|
	|==> compose.yaml
	|
	|==> Dockerfile
	|
	|==> requirements.txt
	|
	|==> web_app.py
	|
	|==> run.sh
	|
	|==> exit.sh 





###############################
Requirements:

1. Proxy Settings

2. docker

###############################

###############
Proxy Settings
###############

To bypassing filtering we run socks5 proxy on localhost:1137 and make changes in following files:

	1. For apt-get:
	
		$ sudo touch /etc/apt/apt.conf.d/95proxies
		
			@ Add following lines to forward request to your proxy:
			
				Acquire::https::proxy "socks5h://127.0.0.1:1137";
				Acquire::http::proxy "socks5h://127.0.0.1:1137";



	2. For docker :
	
		@ Set http and https proxy variables:
		
			$ sudo nano /etc/profile
			
				@ Add following lines:
					
					$ sudo export http_proxy="socks5:/127.0.0.1:1137"
					$ sudo export http_proxy="socks5:/127.0.0.1:1137"
			
		@ To use this variables in sudo environment:

			$ sudo nano /etc/sudoers 		
				Defaults  env_keep += "http_proxy"
				Defaults  env_keep += "https_proxy"			


#############
 docker
#############

####################
 Installation steps
####################

@ Distro: Kali Linux

Steps:


	1. update packe manager:
		$ sudo apt update
	
	2. install docker.io
		$ sudo apt install -y docker.io

	3.Enable docker
		$ sudo systemctl enable docker --now

	4.Do configs for updating apt list:	
		$ echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bookworm stable" | sudo tee /etc/apt/sources.list.d/docker.list 

	5. Get and set GPG: 
		$ curl -fsSL -x socks5h://localhost:1137 https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
		
			@ Note:
				we run socks5 proxy on localhost:1137 for bypassing filtering :)

	6. update packe manager
		$ sudo apt update

	7. install docker-ce docker-ce-cli containerd.io:
		$ sudo apt install -y docker-ce docker-ce-cli containerd.io

	8. Verify installation:
		$ sudo docker run hello-world


####################
 Running Web app
####################

	1. Clone project
		$ git clone https://github.com/sepehr-rp/simple_flask_docker.git

	2. change directory:

		$ cd simple_flask_docker.git

	2. Add permission:
	
		$ sudo chmod 777 run.sh
	
	3. Run Script:
		$ ./run.sh
	
	4. See 127.0.0.1:5000 on your browser
	


####################
 Stop Web app
####################

	1. Stop terminal
		ctrl+c
	
	2. Add permission:
	
		$ sudo chmod 777 exit.sh
	
	3. Run Script:
		$ ./exit.sh





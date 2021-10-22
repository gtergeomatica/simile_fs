Prerequisito: installare docker e docker-compose (per windows docker desktop contiente entrambi) https://docs.docker.com/get-docker/

1. Scaricare i due file Dockerfile e docker-compose.yml (presi da qui https://github.com/web2py/py4web/tree/master/deployment_tools/docker) in una cartella in cui si intende lavorare

2. Aprire il terminale nella cartella in cui sono contenuti i file e lanciare il comando: 
   ```
   docker-compose up -d
   ```
   Dove docker-compose è l'orchestraore (in questo momento non molto utile in quanto abbiamo un solo container) e che tira su l'ambiente (up) in detach mode (-d) quindi in background
   
3. Il container dovrebbe essere creato controllare con:
   ```
   docker ps -a
   ```
   Appuntarsi l'ID del container (prima colonna, tipicamente). Potete accedere a `localhost:8000` a meno che non abbiate cambiato la porta scritta nei file di configurazione di docker;
   
4. Impostiamo la pwd della dashboard da dentro il container (a scopo didattico):
   ```
   docker exec -it <CONTAINER_ID> bash
   ```

5. Lanciamo e impostiamo la pwd:
   ```
   py4web set_password
   ```
   Ora possiamo accedere alla dashboard (lazy-mode on)

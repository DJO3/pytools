# Requirements
1. [Docker Community Edition](https://www.docker.com/community-edition)
    * Tested on Windows 10 Build 15063.540
    * Docker CE Version 17.06.0-ce-win19 (12801)

# Getting Started
1. Log into https://dashboard.stripe.com/account/apikeys and get Secret key.
2. `git clone https://github.com/DJO3/pytools.git`
3. `cd pytools/stripe`
4. Open .env and set STRIPE_TEST to your Secret Key. **Note** This step is required, the current key is not valid. 
5. `docker-compose build`
6. `docker-compose up -d`
7. `docker logs stripe`

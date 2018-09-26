# Califun technical test: Kwikwiter

We just received a very important communication at Califun HQ.
The sender code name is __S.O.B.R.I.N.H.O.__, remind of Califun lead engineer. Seems like he is trying to warn you about a danger...

> **_Schhhttt_** If anybody can hear me, they k... **_Ssshht_**  ...they know! They found out about the secret project! **_Sschhhhttt_** We should have know better... **_Schht_** ...creating the new twitter... **_Schht_** ...we should have known it could be dangerous. They all disappeared... **ALL!** ... I haven't been able to... **_Ssssscchhhhttt_** ...contact agent __K.O.U.T.A.T.A.H__, I don't know if he was able to esca... **_Sshchhhtttchhtt_** HELP **_Sshctt_** US **_Schtt_** ...finish the project before it's too l... **_Schchhththttt_** ...two hours... **_END OF COMMUNICATION_**

I don't know what's going on, but one thing is sure: the future of the company is between __your__ hands... or under your fingers I would say.


## Can you finish kwikwiter in time?

It will be the new Facebook they said... It will be fun they said...
Time is running short. ~~We~~ You have to finish the project and at the same time search for clues to reveal whoever is behind the attack... before they find you.
You are our only hope!

Add features, fix errors and bugs, do your best to improve the website in the short time you have.

* Fork the repository somewhere
* Follow the instruction to launch the project
* Do your work
* Push your work and send us a pull request whenever you feel ready


## Details

* You have here the base of a full django project, similar to what we have on Califun
* Python, Javascript, Django HTML template language and SCSS will be your best weapons here
* You are free to add, modify, fix whatever you want to improve the project. If you need some inspiration, you can for exemple:
⋅⋅* Create a subscribe feature
⋅⋅* Add a comments feature on blog post (and display the number of total comments for a user as a bonus point)
⋅⋅* Store the user initial directly in the datebase instead of computing it at every use (a surcharge of the user model could be smart...)
⋅⋅* Allow the user to delete his post ~~(It happen even to the best of us to post something stupid...)~~
⋅⋅* Add the publication date of a blog post
⋅⋅* Add the number of total likes for a user
⋅⋅* And so on... Do whatever you feel like is needed, you are free. Show us what you got!
* This is not a rush, clean code is always better than feature made too fast. Try to stay under two hours of pure coding, even if you only have one feature, but this is not a strict rule. Feel free to take more time to finish your current feature, just know that we expect more content if you took more time.


## Useful informations

Linux user ~~(Are you a real programmer if you are not on linux tho...)~~:

##### Install Docker:
* sudo apt install docker.io
* sudo apt install docker-compose
* sudo pip install docker-compose

##### Run project:
* sudo docker-compose up

##### Run shell:
* sudo docker-compose run web python manage.py shell

##### Run migration:
* sudo docker-compose run web python manage.py makemigrations 
* sudo docker-compose run web python manage.py migrate

##### User informations:
* Email: johnsnow@kuikuiter.com
* Mot de passe: john1234

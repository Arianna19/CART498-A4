# CART498-A4
https://cart498-a4-r4on.onrender.com
**Project Report: Jugian Dream Interpreter Chat Box**<br>
This assignment asked to design and deploy a web-based dream interpreter tool that analyzes the submitted dreams and generates both a textual and visual interpretation of the dream from the user. The objective was to use Carl Jung's analytical psychology with AI models in a way that's interactive, fun and visually engaging for the users. 

**Jungian Theory Prompt Design**<br>
From what's online, Jung sees dreams as messages from the unconscious, that are shown through symbols, archetypes and reccuring imagery. To accomplish this the best I could, text prompt was designed to guide the AI towards those specific concepts like archetypes, symbolic setting and process individuation. It was difficult to fiddle with the prompt since it had super strict guidelines in terms of coding. Hence, keeping it as simple and short as possible was the best route to take for the AI. Less was more in for the prompting, also due to memory issues. Doing so, the AI produces symbolic, meaningful interpretations and mentions potential inner conflicts or balances the dream from the user shows. 
The image generation portion simply puts the dream description in a symbolic visual scene with some surrealism. This matches Jung's theory of dreams being a metaphor taken from the unconscious. Also, making the image unrealistic is more representitive of what dreams feel like when we experience them.  

**Web App Design and User Guide**<br>
The ChatBox allows users to enter a dream description into a text field. Once they want the dream analyzed, the AI displays what was submitted, shows the Jungian interpretation and a generated image all side-by-side. At first the site was terribly minimal since I was trying to figure out the code and if it deployed correctly through render. I was also learning the memory limitation. Now, the interface is still highly minimal but has a dreamlike-feel thanks to the fuzzy background of gummy bears in clouds and bubble-like containers. All these aspects are to evoke softness and imagination for the user and make the site somewhat pretty without overwhelming the system resources/memory. Shortly said, users type their dream, submit it, have it analyzed and receive an image output all on the same page. 

**Design, Developement and Challenges**<br>
The workflow involved Flask, OpenAI API, Render and GitHub. One major challenge was the deployment on Render, specifically in the memory limitation when generating the images. The early versions I had caused many internal server errors due to worker memory usage within Render logs. I debugged this using both ChatGPT, limiting Gunicorn to a single worker and keeping the CSS terribly simple avoiding visual effects. Another huge challege was debugging, every small code change needed to be pushed on GitHub, waiting for Reender to redeploy the latest commit and then testing live. This made every iteration super slow and often frustrating especially when trying to fix small bugs or slighlty modify the visual look of the site. 

**Testing, Reflection and Improvements**<br>
The ChatBox was tested by submitting multiple dream scenarious to ensure it functioned and generated the image properly. I also tested the same dreams to make sure the analysis were consistent and made sense. The biggest testing phase was for the image generation it took the longest to get it to work to the point I only have $0.42 left in my API to use. If I were to expand on this ChatBox, there could be a image saving feature, multiple interpretation or letting the user choose from a drop-down list another psychologist to analyze the dream. Basically, more pespectives on the dream since it's such an open topic. Overall, this project was mildly frustrating but highlighted creative potential and the limitations of deploying AI-driven sites in real/live environments. So, it was hard to be creative and artistic within the scope of these platforms.

<img width="1885" height="914" alt="image" src="https://github.com/user-attachments/assets/04a4be46-9642-479d-96c7-ce3590e1c666" />





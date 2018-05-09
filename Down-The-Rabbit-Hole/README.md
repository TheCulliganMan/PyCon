# Down the rabbit hole. A 101 on reproducible workflows with Python (aka. HOW TO AVOID MARK CODE)

## Resources

#### Slides

http://bitsandchips.me/Talks/PyCon.html

#### Repos

https://github.com/trallard/ReproduciblePython

#### Setup

http://bitsandchips.me/ReproduciblePython/Setup.html

# Reproducible Work Flows In Python 

## Intro

Reproducability is a chronic problem. Excel for important calculations is like driving drunk.  No matter how careful you are, a wreck is likely.
See: http://science.sciencemag.org/content/334/6060/1226

### Three Pillars:

* Reproducability: Same Code, Same Data, Same Result
* Replicability: Same Data, Different Code, Same Result
* Robustness: Same Data, Different Code, Different Framework (ei. R, C#),  Same Result

### The goals:

1. Complete chain of custody (provenance) from raw data to finished results
2. Always be able to figure out where in your pipeline things broke.

### Practical Use Case:

Everything but data and code is deleted. Run time recovery should be possible.
This decreases the bus factor.  How many people have to get hit before the project grinds to a halt.

### Setting yourself up for success in data science pipelines:

1. What is mvp?
2. Who will use the data and code?
3. How long will this project live.  Open Source? Who will maintain? Where should the data be placed?

### Always Add License

Public != open source
* Permissive --Use these (most open): 
  * MIT 
  * BSD 
  * APACHE 
* CopyLeft --Don't use these unless your project uses packages with GPL: 
  * GPL 
  
### Project Structure

Check out [cookiecutter](https://github.com/audreyr/cookiecutter) It seems like yeoman for python.

Use:

```bash
cookiecutter gh:mkrapp/cookiecutter-reproducible-science
```

Also check out [recipy](https://github.com/recipy/recipy).  Effortless method to record provenance in Python

This could be a really good tool for us to use.


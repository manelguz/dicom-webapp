<div id="top"></div>

  <h3 align="center">Dicom web app</h3>

  <p align="center">
    A Django rest api based webapp to upload and get DICOM images.
    A Cornerstone and jquery based for listing and visualizing previouse uploaded DICOM images 
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



In this project i have design, implementation and deployment of a simple web based medical imaging handler.
Its main features are:

- An API endpoint to upload a DICOM image 
- An API endpoint to list all uploaded DICOM images
- An API endpoint to remove a specific DICOM image
- An API endpoint to download a previously uploaded DICOM image
- A web interface to view a list of all uploaded DICOM images and select one to generate a view for working with the selected ones

The main goal is to train on Django web framework, js web based development and azure deployment.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Django](https://www.djangoproject.com/)
* [Cornerstonejs](https://github.com/cornerstonejs/cornerstone)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to make our project reproductible, we have make use of the python package manager conda.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* conda
  ```sh
  conda env create -f environment.yml
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/manelguz/dicom-webapp.git
   ```
2. Install Anaconda Manager
   ```sh
   wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
   ```
   ```
    bash Anaconda3-2020.02-Linux-x86_64.sh
   ```
3. Install Node package manager
   ```sh
   apt update && apt install npm -y
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

For using the app, the following procedures are avaliable: the standard and the Docker. It is hightly recomended to use the docker ones.

Standard:
  
  ```sh
    # Please set the env vars for the your azure account (AZURE_ACCOUNT_NAME, $AZURE_ACCOUNT_KEY) to fetch the blobs and a given $SECRET_KEY for the django app
    cd dicom-viewer
    cd frontend/ && npm install && npm run-script build
    cd .. && python manage.py migrate && python manage.py collectstatic
    python3 main.py
  ```

Docker:

  ```sh
    docker build --build-arg azure_name=$AZURE_ACCOUNT_NAME --build-arg azure_key=$AZURE_ACCOUNT_KEY  --build-arg django_key=$SECRET_KEY  . -t dicomapp
    docker run -it -p 8080 dicomapp
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Testing -->
## Testing

  ```sh
      coverage run --source='.' manage.py test
      coverage report
  ```

<p align="right">(<a href="#top">back to top</a>)</p>


## Deploy on Axure account
  ```sh
    az webapp up -g $group-name -l westeurope -p $plan-name -r 'PYTHON:3.8'
    az webapp config appsettings set --settings AZURE_ACCOUNT_NAME=$AZURE_ACCOUNT_NAME AZURE_ACCOUNT_KEY=$AZURE_ACCOUNT_KEY SECRET_KEY=$SECRET_KEY
  ```
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Manel Guzmán Castellana - manelguz7@gmail.com


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png


import '../sass/methinks.scss';
import {APIDicom} from './dicom_app'
import {loadDicomImage} from './medicalImageView'
//assets
import MethinksLogo from '../../images/methinks.png';
import backButton from '../../images/back_button.png';


export async function main() {

    var logo = $("<img>").addClass("logo logo-methinks").attr("src", MethinksLogo);
    var title =  $("<h1>").addClass("text-center text-uppercase").text("List of Avaliable image on Server").attr("id","title")
    $("body").append(title);
    $("#header_logo").append(logo);
    
    let dicom_api = new APIDicom();

    const showSelectedImage = (id) => {
      // Function to show the selected dicom image given the image name.

      // Hide the body elements for a cleaner view
      $("body").children().hide();
      // Add the corporate log
      $("#header_logo").show();
      
      // Call the get image method to obtain the image from a given id
      dicom_api.get_img(id)
      .then((img) => {
        
        // Set the View for the dicom image
        $("#dicom-visualizer").show();
        // Load a base64 image
        loadDicomImage(img)
        
        // Set button to come back to the list menu
        let div2 = $("<div>");
        let btn1 = $("<input>").attr("type","image").attr("src",backButton).attr("style","height: 40px").attr("id","backBut")
        div2.append(btn1)
        $("body").append(div2);
        $("#backBut").click(function() {
          $("#dicom-visualizer").hide()
          $("#backBut").remove()
          listAllImages();
        });
      })
    }

    const listAllImages = () => {
       // Add the corporate log and the title app
      $("#header_logo").show();
      $("#title").show();

      // Get all the image name on a server
      dicom_api.list_imgs().then(
        (response) => {
          // For all image name create a clickable element in a list
          let images = response["all_images"]
          let list_img = $("<ul>").attr('id', 'dicom_img_list');
          for (var i = 0; i < images.length; i++) {
            let new_img = $("<li>").addClass("ui-state-default").html(images[i]).attr('style', "cursor:pointer").attr('id', images[i]);
            list_img.append(new_img)
          }
          
          $("body").append(list_img);
          $("#dicom_img_list li").click(function() {
            showSelectedImage(this.id)
          });
        }
      )
    }
    listAllImages()

}

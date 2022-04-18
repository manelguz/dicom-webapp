class APIDicom {
  
    constructor() {
      this.__list_imgs_url = "api/list";
      this.__get_img_url = "api/id";
    }

    list_imgs(){
      return new Promise((resolve, reject) => {
        fetch(this.__list_imgs_url).then((response) => {
          if (response.ok) {
              resolve(response.json())
          } else {
              reject(response.text());
          }
        })
        .catch((err) => { console.log(err); reject(err); });
      });
    }

    get_img(img_id) {
      return new Promise((resolve, reject) => {     
        fetch(`${this.__get_img_url}/${img_id}`).then((response) => {
          if (response.ok) {
            return response.json()
          } else {
            reject(response.text());
          }
        })
        //.then(response => )
        .then(response => {
          resolve(response["dicom_img"])
        })
      })

    }

}

export {
  APIDicom
}
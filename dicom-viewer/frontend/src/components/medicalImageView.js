import * as cornerstone from 'cornerstone-core'
import * as cornerstoneWADOImageLoader from "cornerstone-wado-image-loader";
import * as dicomParser from "dicom-parser";

cornerstoneWADOImageLoader.external.dicomParser = dicomParser;
cornerstoneWADOImageLoader.external.cornerstone = cornerstone;

 const b64toBlob = (b64Data, sliceSize=512) => {
    const byteCharacters = atob(b64Data);
    const byteArrays = [];
  
    for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
      const slice = byteCharacters.slice(offset, offset + sliceSize);
  
      const byteNumbers = new Array(slice.length);
      for (let i = 0; i < slice.length; i++) {
        byteNumbers[i] = slice.charCodeAt(i);
      }
  
      const byteArray = new Uint8Array(byteNumbers);
      byteArrays.push(byteArray);
    }
  
    const blob = new Blob(byteArrays);
    return blob
 }
 


// updates the image display
function updateTheImage(element, imgBase64) {
    const byteImg = b64toBlob(imgBase64)
    const imageId = cornerstoneWADOImageLoader.wadouri.fileManager.add(byteImg);
    return cornerstone.loadAndCacheImage(imageId, byteImg).then(function(image) {
        const viewport = cornerstone.getViewport(element);
        cornerstone.displayImage(element, image, viewport);
    });
}

// setup handlers before we display the image
function onImageRendered(e) {
    const eventData = e.detail;

    // set the canvas context to the image coordinate system
    cornerstone.setToPixelCoordinateSystem(eventData.enabledElement, eventData.canvasContext);

    // NOTE: The coordinate system of the canvas is in image pixel space.  Drawing
    // to location 0,0 will be the top left of the image and rows,columns is the bottom
    // right.

    document.getElementById('topright').textContent = "Render Time:" + eventData.renderTimeInMs + " ms";
    document.getElementById('bottomleft').textContent = "WW/WL:" + Math.round(eventData.viewport.voi.windowWidth) + "/" + Math.round(eventData.viewport.voi.windowCenter);
    document.getElementById('bottomright').textContent = "Zoom:" + eventData.viewport.scale.toFixed(2);
}

const loadDicomImage = (imgBase64) => {
    return new Promise((resolve, reject) => {
        
            // image enable the element
            const element = document.getElementById('dicomImage');
            cornerstone.enable(element);
            element.addEventListener('cornerstoneimagerendered', onImageRendered);
            const imagePromise = updateTheImage(element, imgBase64);
            
            // add handlers for mouse events once the image is loaded.
            imagePromise.then(function() {
        
                // add event handlers to pan image on mouse move
                element.addEventListener('mousedown', function (e) {
                    let lastX = e.pageX;
                    let lastY = e.pageY;
                    const mouseButton = e.which;
        
                    function mouseMoveHandler(e) {
                    const deltaX = e.pageX - lastX;
                    const deltaY = e.pageY - lastY;
                    lastX = e.pageX;
                    lastY = e.pageY;
        
                    if (mouseButton === 1) {
                        let viewport = cornerstone.getViewport(element);
                        viewport.voi.windowWidth += (deltaX / viewport.scale);
                        viewport.voi.windowCenter += (deltaY / viewport.scale);
                        cornerstone.setViewport(element, viewport);
                    } else if (mouseButton === 2) {
                        let viewport = cornerstone.getViewport(element);
                        viewport.translation.x += (deltaX / viewport.scale);
                        viewport.translation.y += (deltaY / viewport.scale);
                        cornerstone.setViewport(element, viewport);
                    } else if (mouseButton === 3) {
                        let viewport = cornerstone.getViewport(element);
                        viewport.scale += (deltaY / 100);
                        cornerstone.setViewport(element, viewport);
                    }
                    }
        
                    function mouseUpHandler() {
                    document.removeEventListener('mouseup', mouseUpHandler);
                    document.removeEventListener('mousemove', mouseMoveHandler);
                    }
        
                    document.addEventListener('mousemove', mouseMoveHandler);
                    document.addEventListener('mouseup', mouseUpHandler);
                });
        
                // Add event handler to the ww/wc apply button
                document.getElementById('x256').addEventListener('click', function (e) {
                    element.style.width = '256px';
                    element.style.height = '256px';
                    cornerstone.resize(element);
                });
        
                document.getElementById('x512').addEventListener('click', function (e) {
                    element.style.width = '512px';
                    element.style.height = '512px';
                    cornerstone.resize(element);
                });
        
                document.getElementById('invert').addEventListener('click', function (e) {
                    const viewport = cornerstone.getViewport(element);
                    viewport.invert = !viewport.invert;
                    cornerstone.setViewport(element, viewport);
                });
        
                /*document.getElementById('interpolation').addEventListener('click', function (e) {
                    const viewport = cornerstone.getViewport(element);
                    viewport.pixelReplication = !viewport.pixelReplication;
                    cornerstone.setViewport(element, viewport);
                });*/
                document.getElementById('hflip').addEventListener('click', function (e) {
                    const viewport = cornerstone.getViewport(element);
                    viewport.hflip = !viewport.hflip;
                    cornerstone.setViewport(element, viewport);
                });
                document.getElementById('vflip').addEventListener('click', function (e) {
                    const viewport = cornerstone.getViewport(element);
                    viewport.vflip = !viewport.vflip;
                    cornerstone.setViewport(element, viewport);
                });
                document.getElementById('rotate').addEventListener('click', function (e) {
                    const viewport = cornerstone.getViewport(element);
                    viewport.rotation += 90;
                    cornerstone.setViewport(element, viewport);
                });
        
                element.addEventListener('mousemove', function(event) {
                    const pixelCoords = cornerstone.pageToPixel(element, event.pageX, event.pageY);
                    document.getElementById('coords').textContent = "pageX=" + event.pageX + ", pageY=" + event.pageY + ", pixelX=" + pixelCoords.x + ", pixelY=" + pixelCoords.y;
                });
                resolve("Image loaded");
            });
        })
}


export {
    loadDicomImage
  }

// The purpose of this file is to allow external svg files to be inserted into the html on page load.
// This allows the svg to be modified dynamically during runtime.

class InsertSVG extends HTMLElement {
    constructor() {
        super();

        
        const link = this.getAttribute("src")
        if(link === ""){
            return
        }
        let xmlhttp = new XMLHttpRequest()
        xmlhttp.onreadystatechange = () => {
            if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                const parent = this.parentElement
                const fragmentDocument = new DOMParser().parseFromString(xmlhttp.responseText, "image/svg+xml")
                const content = fragmentDocument.getElementsByTagName("svg")[0]
                
                this.attributes.removeNamedItem('src')
                for (let i = 0; i < this.attributes.length; i++) {
                    const attribute = this.attributes[i];
                    content.setAttribute(attribute.name, attribute.value)
                }
                parent.insertBefore(content, this)
                this.remove()
            }
        }
        xmlhttp.open("GET", link, true);
        xmlhttp.send()
    }
}

customElements.define('external-svg', InsertSVG);
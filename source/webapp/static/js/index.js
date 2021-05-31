 $.ajaxSetup({
    headers: {
        'X-CSRFToken': getCookie('csrftoken')
    }
});
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log(cookieValue)
    return cookieValue;
}
function quotes(event){
    let block = document.getElementById('container')
    event.stopPropagation()
    $.ajax({
        url: "http://localhost:8000/api/quotes/",
        method: 'GET',
        success: function(data, status) {
            block.innerHTML = ""
            for (let i of data){
                console.log(i)
                block.innerHTML += "<btn type='submit' id='" + i.id + "' onclick='detail(event);'>" + i.text + "</btn> <br>" + " <p> Rating: " + i.rating + "</p>" + "<btn type='submit' id='" + i.id + "' onclick='rate(event);'> + </btn>" + "<btn type='submit' id='" + i.id + "' onclick='unrate(event);'> - </btn>" + "<br>" + "<p>Uploaded: " + i.created_at +  "</p>"
            }
            block.innerHTML += "<a href=''>Go Back</a>"
        },
        error: function(response, status) {
            console.log(status);
        }
        });
}
    function detail(event) {
        let block = document.getElementById('container')
        btnId = event.currentTarget
        event.stopPropagation()
        $.ajax({
            url: "http://localhost:8000/api/quotes/" + btnId.id + "/",
            method: 'GET',
            success: function(data, status) {
            console.log(data)
                 block.innerHTML = "<h2>" +  data.text + "</h2>" + "Rating: " + data.rating + "<p>© " + data.author + "<br>" + data.email + "</p> <br>"
                 block.innerHTML += "<a href=''>Go Back</a>"
            },
            error: function(response, status) {
                console.log(status);
            }
            });
    }

function addQuote(event){
        let block = document.getElementById('container')
         block.innerHTML = '<form id="myForm" action="" method "POST"><input type="text" id="quote" name="quote" value="Quote"><br><br><br><input type="text" id="author" name="author" value="Author"><br><br><input type="email" id="email" name="email" value="E-mail"><br><br><btn type="submit" onclick="add(event);">Add a Quote</btn></form> '
    }
function add(event){
        let myform = document.getElementById("myForm");
        let formData = new FormData(myForm);
        $.ajax({
            url: "",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            type: 'POST',
            success: function () {
            window.alert("Done!");
            }
        });
        }


function rate(event){
    let btnId = event.currentTarget
        $.ajax({
            url: "",
            data: btnId.id,
            cache: false,
            processData: false,
            contentType: false,
            type: 'PUT',
            success: function () {
            window.location.reload()
            window.alert("Rated!");
            },
            error: function(response, status) {
                window.alert("You have already rated it!");
                window.location.reload()
            }
        }
        );
        }
function unrate(event){
    let btnId = event.currentTarget
    let fd = btnId.id
        $.ajax({
            url: "",
            data: fd,
            cache: false,
            processData: false,
            contentType: false,
            type: 'DELETE',
            success: function () {
            window.location.reload()
            window.alert("Rated!");
            },
            error: function(response, status) {
                window.alert("You have already rated it!");
                window.location.reload()
            }
        });
    }
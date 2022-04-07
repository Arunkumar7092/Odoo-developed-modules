var countBox =2;

function addlang()
{
document.getElementById("countlan").value= countBox;

    var newSkill = document.createElement("tr");
        document.getElementById("countlan").value= countBox;
    
        $("#lan").append("<tr> \
            <td><select class='form-control' name='language"+ countBox +"' id='language"+ countBox +"' ' options='{'horizontal': true}'>\
            <option value=''>Select</option>\
            <option value='english'>English</option>\
            <option value='hindi'>HINDI</option>\
            <option value='tamil'>TAMIL</option>\
            <option value='french'>FRENCH</option>\
            <option value='russian'>RUSSIAN</option>\
            <option value='bengali'>BENGALI</option>\
            <option value='telugu'>Telugu</option>\
            <option value='spanish'>SPANISH</option>\
            <option value='portuguese'>PORTUGUESE</option>\
            <option value='chinese'>CHINESE</option>\
            <option value='japanese'>JAPANESE</option>\
            <option value='arabic'>ARABIC</option>\
            <option value='urudu'>URUDU</option>\
            <option value='punjabhi'>PUNJABHI</option>\
            <option value='korean'>KOREAN</option>\
            <option value='turkish'>TURKISH</option>\
            <option value='german'>GERMAN</option>\
            </select></td>\
            ");

        countBox += 1;
}

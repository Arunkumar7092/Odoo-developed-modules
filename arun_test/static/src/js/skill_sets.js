var countBox =2;

function addskill()
{
document.getElementById("countskl").value= countBox;

    var newSkill = document.createElement("tr");
        document.getElementById("countskl").value= countBox;
    
        $("#skl").append("<tr> \
            <td><select class='form-control' name='employee_skills"+ countBox +"' id='employee_skills"+ countBox +"' ' options='{'horizontal': true}'>\
            <option value=''>Select</option>\
            <option value='odoo'>ODOO</option>\
            <option value='python'>Python programming Language</option>\
            <option value='java'>Java programming Language</option>\
            <option value='c'>C programming Language</option>\
            <option value='c++'>C ++ programming Language</option>\
            <option value='oops'>Objects Orieneted programming Language</option>\
            <option value='machine learning'>Machine Learning</option>\
            <option value='c#'>c#</option>\
            <option value='html'>HTML and CSS</option>\
            <option value='iot'>Interenet of Things</option>\
            <option value='sap'>SAP</option>\
            <option value='odooerp'>ODOO ERP</option>\
            <option value='sales'>Sales Management</option>\
            <option value='data'>Data Analysis</option>\
            <option value='team'>Team Leadership</option>\
            <option value='communication'>Good Communication</option>\
            <option value='order'>Order To Cash</option>\
            <option value='pogramming'>Programming</option>\
            <option value='linux'>Linux</option>\
            <option value='arudino'>Arduino</option>\
            <option value='electical'>Electrical and Electronics</option>\
            <option value='industry'>Industry</option>\
            <option value='chemical'>Chemical</option>\
            <option value='networking'>Networking</option>\
            </select></td>\
            ");

        countBox += 1;
}

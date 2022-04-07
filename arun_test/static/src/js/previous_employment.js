var countBox =2;

function addExp()
{
document.getElementById("countexp").value= countBox;

    var newChild = document.createElement("tr");
        document.getElementById("countexp").value= countBox;
    
        $("#exp").append("<tr> \
            <td><input type='text' class='form-control' id='empployment_name"+ countBox +"'  \
            name='empployment_name"+ countBox+"'/></td>\
            <td><input type='text' class='form-control' id='employment_id"+ countBox +"'  \
            name='employment_id"+ countBox+"'/></td>\
            <td><input type='text' class='form-control' id='empployment_title"+ countBox +"'  \
            name='empployment_title"+ countBox+"'/></td>\
    		<td><input type='date' class='form-control' id='from_date"+ countBox +"'  \
            name='from_date"+ countBox+"'/></td>\
            <td><input type='date' class='form-control' id='To_date"+ countBox +"'  \
            name='To_date"+ countBox+"'/></td>\
            <td><input type='number' class='form-control' id='employment_salary"+ countBox +"'  \
            name='employment_salary"+ countBox+"'/></td>\
            <td><input type='text' class='form-control' id='employment_resignation"+ countBox +"'  \
            name='employment_resignation"+ countBox+"'/></td>\
            <td><input type='text' class='form-control' id='empployment_address"+ countBox +"'  \
            name='empployment_address"+ countBox+"'/></td>\
            ");

        countBox += 1;
}

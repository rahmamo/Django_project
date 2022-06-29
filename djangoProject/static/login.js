function validateForm(ev,ele){
    ev.preventDefault();
    var frist_name=document.forms[0].elements[0].value;
    var Last_name =document.forms[0].elements[1].value;
    var Email=document.forms[0].elements[2].value;
    var Password=document.forms[0].elements[3].value;
    var Confirm_Password=document.forms[0].elements[4].value;
    var Mobile_Number=document.forms[0].elements[5].value;
    var pattern_name=/^([A-Za-z]{3,})*$/;
    var pattern_email=/^[A-Za-z0-9]+@[a-z0-9]+[.]([a-z]{2,3})$/;
    var pattern_mobile=/^[0][1][1|2|5|0]+([0-9]{8})*$/;
    f_test=pattern_name.test(frist_name);
    l_test=pattern_name.test(Last_name);
    m_test=pattern_email.test(Email);
    n_test=pattern_mobile.test(Mobile_Number);
    consel.log("aa")
    var p_test=false
    if(Password == Confirm_Password){ p_test=true }
    if(f_test == true && l_test == true && m_test == true && n_test == true && p_test == true ){
        ele.submit()
    }
    else{
        document.getElementById("error").innerHTML = "the inforamtion is error" 
    }
}



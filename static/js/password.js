function seePassWord(){
    var password_ = document.getElementById('id_password');
    console.log(password_.type)
    if (password_.type === 'password'){
        console.log('yes')
        password_.type = 'text';
    }else{
        password_.type = 'password';
    }
}
function seePassWord2(){
    var password_ = document.getElementById('id_password_');
    console.log(password_.type)
    if (password_.type === 'password'){
        console.log('yes')
        password_.type = 'text';
    }else{
        password_.type = 'password';
    }
};

var password = document.getElementById('id_password_');
console.log(password)

password.addEventListener('keyup', function(e){
    var pass = document.getElementById('id_password').value;
    var pass_ = document.getElementById('id_password_').value;
    if (pass != pass_){
        
        document.getElementById('no-match').classList.remove('hidden');
        document.getElementById('id_password_').classList.add('is-invalid')

    }else{
        document.getElementById('no-match').classList.add('hidden');
        document.getElementById('id_password_').classList.remove('is-invalid')
    }
})

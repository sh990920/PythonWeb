// 아이디 중복 검사를 위한 변수
let idCheck = false;

// 닉네임 중복 검사를 위한 변수
let nicknameCheck = false;

// 비밀번호 중복 검사를 위한 변수
let isPasswordEqualse = false;

// 비밀번호 유효성 검사
function pwdCheck(f) {
    let pwd = f.password.value;
    let pwdText1 = document.getElementById("pwdText1");

    let pattern1 = /[0-9]/; // 숫자 입력
    let pattern2 = /[a-zA-Z]/; // 영어 소문자, 대문자 입력
    let pattern3 = /[~!@#$%^&*()_+]/; // 특수기호 입력

    if ( !pattern1.test(pwd) || !pattern2.test(pwd) || !pattern3.test(pwd) || pwd.length < 5 ) {
        pwdText1.innerHTML = "영문, 숫자, 특수기호(~!@#$%^&*()_+)를 포함하여 5자리 이상으로 구성하여야 합니다";
    } else {
        pwdText1.innerHTML = "";
    }
}

// 비밀번호 재 입력시 일치하는지 검사
function pwdCheck2(f) {
    let pwd = f.password.value;
    let pwd2 = f.passwordCheck.value;
    let pwdText2 = document.getElementById("pwdText2");

    if ( pwd2 != pwd ) {
        pwdText2.innerHTML = "비밀번호가 일치하지 않습니다";
        isPasswordEqualse = false;
    } else {
        pwdText2.innerHTML = "";
        isPasswordEqualse = true;
    }
}

// 아이디 중복 검사
function checkId(){
    let memberId = document.getElementById("memberId").value;
    if(memberId == ''){
        alert("아이디를 입력해주세요");
        return;
    }
    let url = "/member/idCheck";
    let param = "memberId=" + memberId;
    sendRequest(url, param, resId, "GET");
}

// ajax로 받아온 HttpResponse를 처리
function resId(){
    let memberIdTag = document.getElementById("memberId");
    if ( xhr.readyState == 4 && xhr.status == 200 ) {
        var data = xhr.responseText;
        if(data == 'no') {
            alert('아이디 중복');
            return;
        } else {
            alert('아이디 중복 없음');
            memberIdTag.readOnly = true;
            idCheck = true;
        }
    }
}

// 닉네임 중복 검사
function checkNickname(){
    let nickname = document.getElementById("nickname").value;
    let nicknameCheck = document.getElementById("nicknameCheck");
    if ( nickname.length > 20 ) {
        nicknameCheck.innerHTML = "닉네임은 10자내로 작성해주세요 (영문만 작성시 20자까지 가능합니다.)";
        return;
    }
    if(nickname == ''){
        alert("닉네임을 입력해주세요");
        return;
    }
    let url = "/member/nicknameCheck";
    let param = "nickname=" + nickname;
    sendRequest(url, param, resNickname, "GET");
}

// HttpResponse를 처리
function resNickname(){
    let nicknameTag = document.getElementById("nickname");
    if ( xhr.readyState == 4 && xhr.status == 200 ) {
        var data = xhr.responseText;
        if(data == 'no') {
            alert('닉네임 중복');
            return;
        } else {
            alert('닉네임 중복 없음');
            nicknameTag.readOnly = true;
            nicknameCheck = true;
        }
    }
}

// 회원가입 진행
function signUp(f){
    let memberId = f.memberId.value;
    let password = f.password.value;
    let nickname = f.nickname.value;
    let like_category = f.like_category.value;

    if(idCheck != true){
        alert("아이디 중복검사를 진행하세요");
        return;
    }
    if(isPasswordEqualse != true){
        alert("비밀번호가 일치하지 않습니다.");
        return;
    }
    if(nicknameCheck != true){
        alert("닉네임 중복검사를 진행하세요");
        return;
    }
    let url = "/member/signUp/";
    let param = "memberId=" + memberId +
                "&password=" + password +
                "&nickname=" + nickname +
                "&like_category=" + like_category;
    sendRequest(url, param, resSignUp, "POST");
}

// HttpResponse 처리
function resSignUp(){
    if ( xhr.readyState == 4 && xhr.status == 200 ) {
        var data = xhr.responseText;
        if(data == 'no') {
            alert('회원가입 실패');
            return;
        } else {
            alert('회원가입 성공');
            location.href= "/";
        }
    }
}
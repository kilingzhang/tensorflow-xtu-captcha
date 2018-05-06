<?php



function httpPost($url , $post_data){
 

    $opts = array('http' =>
                      array(
                          'method' => 'POST',
                          'header' => 'Content-type: application/x-www-form-urlencoded',
                          'content' => http_build_query($post_data)
                      )
    );
    $context = stream_context_create($opts);
    $result = file_get_contents($url, false, $context);
    return $result;
}


$url = 'http://jwxt.xtu.edu.cn/verifycode.servlet';

$start = 1;
$count = 250;

$path = './test/';

for ($i=$start; $i <= $count; $i++) { 
    $img = file_get_contents($url);
    
    $name = $path . $i . '.jpg';

    file_put_contents($name , $img);

    $fuckUrl = 'https://api.sky31.com/edu_idcode.php?role=2015551439&hash=hash';
    
    $post_data = array(
        'data' => base64_encode($img),
    );



    $text = httpPost($fuckUrl,$post_data);


    if(json_decode($text,true)['code'] != 0){
       $i--;
       continue;
    }

    if(json_decode($text,true)['code'] == 0){
        $text = json_decode($text,true)['idcode'];
    }

    file_put_contents('./test.txt' , $name . ':' . $text . "\n", FILE_APPEND);

    echo $i . "\n" ;
}



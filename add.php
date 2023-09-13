<!DOCTYPE html>
<html>
    <head>
        <title>Add Data</title>
    </head>
    <?php
        $db_pointer = $this->open("main.db");
        $result = $db_pointer->query("SELECT * FROM show");
        var_dump($result->fetch_array());
    ?>
    <body>
        <h2>Add Songs</h2>
        1. <input type="text">
    </body>
</html>
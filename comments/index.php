<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comments</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="container">
        <main class="main">
            <header>
                <h1>Comment section</h1>
            </header>
            <section>
                <form class="main-form" action="addcomment.php" method="post" id="add_comment_form">
                    <label for="username">Enter username</label>
                    <input id="username" type="text" name="username" required>
                    <label for="comment">Enter comment</label>
                    <textarea id="comment" rows="4" cols="50" name="comment" required></textarea>
                    <button type="submit">Submit</button>
                </form>
            </section>
            <section class="comment-section">
                <?php
                $servername = "localhost";
                $username = "root";
                $password = "";
                $db = "comment_system";
                $connect = mysqli_connect($servername, $username, $password, $db);
                $query = " SELECT * FROM comments";
                $sql = mysqli_query($connect, $query);
                while ($row = mysqli_fetch_row($sql)) {
                    echo "<div class=\"comment\">",
                    "<h2>",
                    $row[1], "</h2>",
                    "<p>",
                    $row[2],
                    "<br> ",
                    $row[3],
                    " </p></div>";
                }
                ?>
            </section>
        </main>
    </div>
</body>

</html>
<?php
include('server/header.php');
//header('Location: http://google.co.ve');

print_r($_GET);
 ?>

<table>
    <?php foreach ($_SERVER as $key => $value): ?>
        <tr>
            <td><?php echo $key; ?></td>
            <td><?php echo $value; ?></td>
        </tr>
    <?php endforeach; ?>
</table>

<?php

print_r(headers_list());
include('server/footer.php');

 ?>

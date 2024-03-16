<?php
// Define the password to unlock the PDF
$correctPassword = "your_password_here";

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the password entered by the user
    $enteredPassword = $_POST["password"];

    // Check if the entered password matches the correct password
    if ($enteredPassword == $correctPassword) {
        // Set the headers to force download the PDF
        header('Content-Type: application/pdf');
        header('Content-Disposition: attachment; filename="protected.pdf"');

        // Read the PDF file
        $file = 'OSEB CHARGES.pdf';
        readfile($file);

        // Exit the script
        exit;
    } else {
        // Password is incorrect, redirect back to the form
        header("Location: index.html");
        exit;
    }
} else {
    // If the form is not submitted, redirect back to the form
    header("Location: index.html");
    exit;
}
?>

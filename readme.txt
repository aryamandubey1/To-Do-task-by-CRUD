<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jarvis</title>
</head>

<body>

</body>
</html>
========================]
todo              ======]
todo1234          ======]
========================]

/*------Login------*/

body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
  }
  
  .form-inner {
    width: 400px;
    padding: 40px;
    background: #fff;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    border-radius: 8px;
  }
  
  .field {
    position: relative;
    margin-bottom: 20px;
  }
  
  .field input[type="text"],
  .field input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: 16px;
  }
  
  .pass-link {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 20px;
  }
  
  .pass-link a {
    color: #0066cc;
    text-decoration: none;
    font-size: 14px;
  }
  
  .field.btn {
    position: relative;
    overflow: hidden;
  }
  
  .field.btn .btn-layer {
    position: absolute;
    height: 100%;
    width: 300%;
    left: -100%;
    background: linear-gradient(120deg, #3498db, #8e44ad, #3498db, #8e44ad);
    transition: all 0.4s ease;
  }
  
  .field.btn {
    position: relative;
    display: inline-block;
}

.btn-layer {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #007bff; /* Button background color */
    border-radius: 5px; /* Optional: rounded corners */
    z-index: 1; /* Below the input field */
    pointer-events: none; /* Allows clicks to pass through */
}

input[type="submit"] {
    position: relative;
    z-index: 2; /* Above the btn-layer */
    background: transparent; /* No background to show btn-layer color */
    color: #fff; /* Text color */
    border: none;
    cursor: pointer;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px; /* Optional: match btn-layer */
    text-align: center;
}

  
  .login {
    text-align: center;
    margin-top: 20px;
  }
  
  .login a {
    color: #0066cc;
    text-decoration: none;
    font-size: 14px;
  }
  

  /*------rehister----*/

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
  }
  
  .form-inner {
    width: 400px;
    padding: 40px;
    background: #fff;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    border-radius: 8px;
  }
  
  .field {
    position: relative;
    margin-bottom: 20px;
  }
  
  .field input[type="text"],
  .field input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: 16px;
  }
  
  .field.btn {
    position: relative;
    overflow: hidden;
  }
  
  .field input[type="submit"] {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 4px;
    color: #fff;
    background-color: #3498db;
    cursor: pointer;
    font-size: 18px;
    transition: background-color 0.4s ease;
  }
  
  .field input[type="submit"]:hover {
    background-color: #2980b9;
  }
  
  .field.btn .btn-layer {
    position: absolute;
    height: 100%;
    width: 300%;
    left: -100%;
    background: linear-gradient(120deg, #3498db, #8e44ad, #3498db, #8e44ad);
    transition: all 0.4s ease;
  }
  
  .field.btn input[type="submit"]:hover .btn-layer {
    left: 0;
  }
  
  .register {
    text-align: center;
    margin-top: 20px;
  }
  
  .register a {
    color: #0066cc;
    text-decoration: none;
    font-size: 14px;
  }
  
                                     <tr>
                                        <td>Renew car insurance</td>
                                        <td>In Progress</td>
                                        <td>
                                            <button type="submit" class="btn btn-danger">Delete</button>
                                            <button type="submit" class="btn btn-success ms-1">Finished</button>
                                        </td>
                                    </tr>
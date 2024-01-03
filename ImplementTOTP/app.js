const Express = require("express");
const BodyParser = require("body-parser");
const Speakeasy = require("speakeasy");

var app = Express();

app.use(BodyParser.json());
app.use(BodyParser.urlencoded({ extended: true }));

// Hardcoded secret key
const hardcodedSecret = "ZYTYYE5FOAGW5ML7LRWUL4WTZLNJAMZS";

app.post("/totp-secret", (request, response, next) => {
    console.log("Received request for /totp-secret");
    console.log("Sending hardcoded secret:", hardcodedSecret);
    response.send({ "secret": hardcodedSecret });
});

app.post("/totp-generate", (request, response, next) => {
    console.log("Received request for /totp-generate");
    console.log("Generating TOTP token...");
    try {
        const token = Speakeasy.totp({
            secret: hardcodedSecret,
            encoding: "base32"
        });
        console.log("Generated TOTP token:", token);

        const remaining = 30 - Math.floor(new Date().getTime() / 1000.0 % 30);
        console.log("Remaining seconds:", remaining);

        response.send({ "token": token, "remaining": remaining });
    } catch (error) {
        console.error("Error generating TOTP token:", error.message);
        response.status(500).send({ "error": "Internal Server Error" });
    }
});

app.post("/totp-validate", (request, responce, next) => {
    console.log("Received request for /totp-validate");
    console.log("Validating TOTP token...");
    try {
        const valid = Speakeasy.totp.verify({
            secret: hardcodedSecret,
            encoding: "base32",
            token: request.body.token,
            window: 0
        });
        console.log("Token validation result:", valid);

        responce.send({ "valid": valid });
    } catch (error) {
        console.error("Error validating TOTP token:", error.message);
        responce.status(500).send({ "error": "Internal Server Error" });
    }
});

app.listen(3000, () => {
    console.log("Listening at : 3000...");
});

from Views.Error import display_error

class ErrorController:

    usb_key_not_found_message: str = "Please insert the USB key"
    
    @staticmethod
    def handle_usb_not_found():
        display_error(ErrorController.usb_key_not_found_message)
        raise FileNotFoundError(ErrorController.usb_key_not_found_message)

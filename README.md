# Anglesey-Cleaners
Give me the full models  . General Locations will be a list of town / cities in the local area (This decides what area the customer is in when they signup so it only shows staff cleaners in that area or that service that area ) then specific postcodes of staff, customers and house numbers , street names etc Must be in Typical Welsh post code format.   1 Owner must approve staff, view all information of the booking system, . See all transaction amounts , dates , staff data and customer contact info and location . Can delete staff and cancel appointments . Issue refunds .                 2 Staff can select locations they service , contact info email phone number , expected hourly rate . Travel costs associated with different locations that they select . Image of staff . They will also hold a 5 star rating that has 1 5 star vote on starting then customers can rate staff once booked . Customers should pay the transport cost ahead of the booking.  Customers should include their contact number and email address. The booking system should show once customers sign up they will only enter payment information once viewing the system and selecting a specific staff member who services that area and is available at that time . They should also state how long it takes . When they do that staff member becomes unavailable at those times . This is also reflected on the staff members page . All appointment dates will be updated to the owners view of every staff member with their username and ranking . [Give me all the models ] 



Issue with redirect potential solutions 
HSTS prevents accidental redirects: By enforcing HTTPS connections, browsers are instructed to only communicate with your website using secure connections. This eliminates the possibility of redirects to the non-secure version, which might not preserve the original URL.
Removing app name from URL: Setting the X-Forwarded-Host header instructs the application to use the domain name from the original request instead of its internal subdomain. This ensures that the URL displayed in the browser matches your custom domain throughout the user experience.
However, it's important to note that:

Testing is crucial: After implementing these changes, thoroughly test your website across different browsers and devices to ensure everything functions as expected and the desired URL structure is maintained.
Potential edge cases: In rare cases, specific browser configurations or network setups might still cause unexpected behavior. Monitor your website and address any issues that arise.
Additional factors to consider:

Correct configuration: Ensure both HSTS and X-Forwarded-Host header are configured correctly based on your specific web framework and Heroku setup. Refer to Heroku's documentation and your framework's guidelines for detailed instructions.
Code updates: If changes are made to your application code or deployment environment, revisit these configurations to ensure they remain valid and functional.



Existing Cases of Successfully Preventing Redirects with HSTS and Removing App Name on Heroku
Here are some examples of successful implementations where users combined HSTS and removing the app name from the URL to prevent redirects on Heroku with custom domains:

1. Stack Overflow Discussion:

A Stack Overflow thread discusses similar challenges with redirects and offers solutions involving HSTS and X-Forwarded-Host header configuration. Users report success in achieving seamless user experience with their custom domains. (https://stackoverflow.com/questions/35883929/why-does-a-custom-domain-redirect-to-herokuapp-com)
2. Blog Post:

A blog post by "DigitalOcean" outlines various approaches to removing the app name from the URL on Heroku, including setting the X-Forwarded-Host header. The post mentions the effectiveness of this method in combination with HSTS for maintaining desired URL structure. (https://www.digitalocean.com/community/questions/in-app-platform-a-custom-domain-was-configured-but-no-https-certificate-generated-how-come)
3. Heroku Dev Center:

While not explicitly focusing on preventing redirects, the Heroku Dev Center documentation provides detailed instructions on enabling HSTS and setting the X-Forwarded-Host header. These configurations contribute to maintaining the desired URL structure when using custom domains. (https://devcenter.heroku.com/articles/custom-domains)
4. GitHub Repositories:

Searching on GitHub for open-source projects deployed on Heroku with custom domains can reveal examples of successful implementations. Look for projects that mention HSTS and X-Forwarded-Host configuration in their code or documentation.

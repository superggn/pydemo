 const clientId = '905804377606-2hfg5p2dsht9o528ckrt0r27bc20cn66.apps.googleusercontent.com';
 const redirectUri = 'https://fe-1n-test.trustdice.win/';
 const GOOGLE_REDIRECT_URI = redirectUri; // Or replace with your actual value
 const scope = 'https://www.googleapis.com/auth/userinfo.email';
 const state = 'wozhaoritianzuiniubi';

 const rawGetParams = {
     response_type: 'code',
     client_id: clientId, // Replace `clientId` with your actual client ID
     redirect_uri: GOOGLE_REDIRECT_URI,
     scope: scope,
     state: state,
     access_type: 'offline',
     include_granted_scopes: 'true',
     // login_hint: 'hint@example.com',
     prompt: 'consent',
 };

 // Function to encode parameters as a query string
 const urlencode = (params) => {
     return Object.keys(params)
         .map(key => `${encodeURIComponent(key)}=${encodeURIComponent(params[key])}`)
         .join('&');
 };

 const encodedParams = urlencode(rawGetParams);
 const authorizationUrl = 'https://accounts.google.com/o/oauth2/auth?' + encodedParams;

 console.log(authorizationUrl);

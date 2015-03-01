package com.deere.democlient;

import com.deere.rest.OAuthClient;
import com.deere.rest.OAuthToken;

public abstract class ApiCredentials {
    
    public static final OAuthClient CLIENT = new OAuthClient("johndeere-I7I0N4IhW55I3PJDqQkAS1Ya", "0a7f3fd08fe5f0fff2bd99885ce876fb2f35f65c");
    
    public static final OAuthToken TOKEN = new OAuthToken("c1728df1-d074-4044-a3ad-9cc629509c23", "5pLhvFcDLL2Qwfjp6nJ0831iVegdVbBdULwPx26BeBh/J0xB94wKW6PIsSLuoVN9fKB4BCEhNljOfmNzG6XGGJWiSdYvvzA3dEm7i4hVWt4=");
}

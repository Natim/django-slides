module Main exposing (main)

import Browser
import Html exposing (..)
import Html.Attributes exposing (attribute)


goodMap : List (Attribute a) -> List (Html a) -> Html a
goodMap =
    Html.node "good-map"


main =
    goodMap
        [ attribute "api-key" "AIzaSyCwFpb-7egXk83gMwyuofJZrkIP4XlgD28"
        , attribute "latitude" "48.106661"
        , attribute "longitude" "-1.694661"
        , attribute "zoom" "17"
        ]
        []

import elmWebComponents from '@teamthread/elm-web-components'
import {Elm} from './Main.elm'

elmWebComponents.configure('0.19')

elmWebComponents.register('my-elm-component', Elm.Main)

import {Header, Link} from "@vkontakte/vkui";
import {header} from "../styles/common";
import Image from "next/image";
import logo from "../styles/logo.png";
import {getUserCard} from "./interfaceHelpers";
import {fetchAPI} from "./helpers";

export async function getServerSideProps(context) {
    const DATA_URL = '/users/me/';
    console.log('here')
    const data = await fetchAPI(context, DATA_URL);
    console.log('data', data);
    return {
        props: {},
    }
}

export const GarageHeader = ({ user }) => (
    <Header mode="primary">
        <div style={ header }>
            <Image
                src={ logo }
                width={ 70 }
                height={ 70 }
            />
            <Link href="/" style={{ margin: '0 20px'}}>Все объявления</Link>
            <Link href="/item/my/" style={{ margin: '0 20px'}}>Мои объявления</Link>
            <Link href="/item/create/" style={{ margin: '0 20px' }}>Добавить</Link>
            { user && getUserCard(user) }
        </div>
    </Header>
);

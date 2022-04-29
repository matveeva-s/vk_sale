import {
    View,
    Panel,
    Group,
    ContentCard,
    CardGrid,
    Link,
} from "@vkontakte/vkui";
import { fetchAPI } from '../helpers';
import { smallCard } from "../../styles/common";
import { getItemPrice } from '../interfaceHelpers';

export async function getServerSideProps(context) {
    const DATA_URL = '/store/items/filtered/my/';
    const data = await fetchAPI(context, DATA_URL);
    return {
        props: {items: data.results},
    }
}

export default function Main(props) {
    const cards = props.items.map(
        item => {
            const content = (
                <div>
                    { item.preview && <img src={ item.preview } style={ smallCard.image } /> }
                    <div>{ getItemPrice(item) }</div>
                </div>
            )
            return (
                <ContentCard
                    key={item.id}
                    header={
                        <Link
                            style={ smallCard.title }
                            href={`/item/${item.id}/`}>
                            { item.title }
                        </Link>
                    }
                    style={ smallCard }
                    text={ content }
                />
            )
        }
    )
    return (
        <View activePanel="main">
            <Panel id="main">
                <Group>
                    <CardGrid style={{padding: '20px'}} size="s">
                        { !!cards.length ? cards : 'Тут пока ничего нет 🐝' }
                    </CardGrid>
                </Group>
            </Panel>
        </View>
    )
}

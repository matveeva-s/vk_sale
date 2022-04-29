import {
    Gallery, Group, Panel, View, Card, CardGrid, Title, Div, Text, Button, Header, SimpleCell, InitialsAvatar, Link,
} from '@vkontakte/vkui';
import { fetchAPI } from '../helpers';
import { itemCard, header, coin } from '../../styles/common';
import {getItemPrice, getUserCard} from '../interfaceHelpers';

export async function getServerSideProps(context) {
    const DATA_URL = `/store/items/${context.params.id}/`;
    const data = await fetchAPI(context, DATA_URL);
    return {
        props: { item: data },
    }
}

export default function DetailedItemPage({ item }) {
    const seller = () => (
        <div style={{ marginTop: '-6px' }}>
            { getUserCard(item.seller) }
        </div>
    );

    return (
        <View activePanel="main">
            <Panel id="main">
                <CardGrid>
                    {!!item.images?.length  &&
                        <Card mode="shadow">
                            <Gallery
                                style={{ height: itemCard.height }}
                                bullets="dark"
                                showArrows
                            >
                                { item.images.map(image => (
                                    <img
                                        key={ image.id }
                                        className="carousel-image"
                                        src={ image.image }
                                        alt="Тут картинка"
                                    />
                                )) }
                            </Gallery>
                        </Card>
                    }
                    <Card mode="shadow" style={{ flexGrow: 1, height: itemCard.height }}>
                        <Div style={ itemCard.content }>
                            <Title style={ itemCard.title }>
                                { item.title }
                                { seller() }
                            </Title>
                            <Text style={ itemCard.description }>
                                { item.description }
                            </Text>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                                { getItemPrice(item) }
                                <Button
                                    size='l'
                                    style={ itemCard.button }
                                    label="Написать продавцу"
                                >
                                    <Link href={ item.seller.contact } style={{ color: "white"}}>
                                        Написать продавцу
                                    </Link>
                                </Button>
                            </div>
                        </Div>
                    </Card>
                </CardGrid>
            </Panel>
        </View>
    );
};

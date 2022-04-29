import {
    View,
    Panel,
    Group,
    ContentCard,
    CardGrid,
    Link,
    FormItem,
    Select,
    SplitLayout,
    SplitCol,
    PanelHeader,
} from "@vkontakte/vkui";
import { useState } from 'react';
import {fetchAPI, reactFetchAPI} from './helpers';
import {itemCard, smallCard} from "../styles/common";
import { getItemPrice } from './interfaceHelpers';

export async function getServerSideProps(context) {
    const itemsData = await fetchAPI(context, '/store/items/');
    const categoriesData = await fetchAPI(context, '/store/categories/');
    return {
        props: {
            items: itemsData.results,
            categories: categoriesData,
        },
    }
}

export default function Main(props) {
    const [items, setItems] = useState(props.items);

    const onChange = async (event) => {
        const itemsData = await reactFetchAPI(`/store/items/?category=${event.currentTarget.value}`);
        setItems(itemsData.results);
    };

    const cards = items.map(
        item => {
            const content = (
                <div>
                    { item.preview && <img src={ item.preview } style={ smallCard.image } /> }
                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                        { getItemPrice(item) }
                        <div style={ itemCard.price }>{ item.category }</div>
                    </div>
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
                <SplitLayout>
                    <SplitCol fixed width={280} maxWidth={280} style={{ marginRight: 16 }}>
                        <Group>
                            <FormItem top="Категория товара">
                                <Select
                                    placeholder="Не выбран"
                                    options={ props.categories.map(c => ({ value: c.id, label: c.name })) }
                                    onChange={ onChange }
                                />
                            </FormItem>
                        </Group>
                    </SplitCol>
                    <SplitCol>
                        <Panel>
                            <PanelHeader>Товары</PanelHeader>
                            <Group>
                                <CardGrid style={{padding: '20px'}} size="s">
                                    { cards }
                                </CardGrid>
                            </Group>
                        </Panel>
                    </SplitCol>
                </SplitLayout>
            </Panel>
        </View>
    )
}

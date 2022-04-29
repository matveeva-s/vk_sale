import {
    FormLayout,
    FormItem,
    PanelHeader,
    Group,
    Input,
    View,
    Panel,
    Textarea,
    File,
    Button,
    Select,
} from "@vkontakte/vkui";
import { Icon24Camera } from "@vkontakte/icons";
import React, { Component } from 'react';
import styles from '../../styles/create_item.module.css';
import { form } from '../../styles/common';
import {fetchAPI, reactFetchAPI} from "../helpers";

async function sendNewAdvert(itemData, categories) {
    const DATA_URL = '/store/items/';
    const IMAGES_URL = itemId => `/store/items/${itemId}/images_save/`;
    const sendData = {...itemData, category: categories[parseInt(itemData.category)-1]}
    const data = await reactFetchAPI(
        DATA_URL, 'POST', JSON.stringify(sendData),
    ).then((resp) => {
        let fd = new FormData();
        itemData.selectedFiles.forEach(file => {
            fd.append('images', file);
        });
        reactFetchAPI(IMAGES_URL(resp.id), 'POST', fd, 'formdata');
    });
    return {
        props: {item: data},
    }
}

export async function getServerSideProps(context) {
    const categoriesData = await fetchAPI(context, '/store/categories/');
    return {
        props: {
            categories: categoriesData,
        },
    }
}

export default class CreateForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            title: '',
            category: null,
            description: '',
            price_rub: null,
            price_coins: null,
            selectedFiles: []
        }
        this.fileInput = React.createRef();
    }
    handleTitleChange = (event) => {
        this.setState({title: event.target.value});
    }
    handleDescriptionChange = (event) => {
        this.setState({description: event.target.value});
    }
    handleFileChange = (event) => {
        this.setState({ selectedFiles: [...this.state.selectedFiles, ...this.fileInput.current.files] });
    }
    handlePriceRubChange = (event) => {
        this.setState({price_rub: event.target.value});
    }
    handlePriceCoinsChange = (event) => {
        this.setState({price_coins: event.target.value});
    }
    handleSubmit = (event) => {
        sendNewAdvert(this.state, this.props.categories);
        event.preventDefault();
    }

    handleCategoryChange = (event) => {
        this.setState({category: event.target.value});
    }

    render () {
        const previews = Array.from(this.state.selectedFiles).map(
            (image) => {
                const url = URL.createObjectURL(image);
                return <img key={ image.name } src={ url } width={ 50 } height={ 50 } className={ styles.previewImage} />;
            }
        );
        return(
            <View activePanel="create_form">
                <Panel id="create_form" style={{ width: '70%', margin: 'auto'}}>
                    <PanelHeader>Добавить что-то для продажи</PanelHeader>
                    <Group>
                        <FormLayout onSubmit={ this.handleSubmit }>
                            <FormItem>
                                <div style={ form.label }>Заголовок</div>
                                <Input value={ this.state.title} onChange={ this.handleTitleChange } />
                            </FormItem>
                            <FormItem>
                                <div style={ form.label }>Категория</div>
                                <Select
                                    value={ this.state.category}
                                    onChange={ this.handleCategoryChange }
                                    options={ this.props.categories.map(c => ({ value: c.id, label: c.name })) }
                                />
                            </FormItem>
                            <FormItem>
                                <div style={ form.label }>Описание</div>
                                <Textarea
                                    value={ this.state.description }
                                    onChange={ this.handleDescriptionChange }
                                />
                            </FormItem>
                            <FormItem>
                                <div style={ form.label }>Цена (в рублях)</div>
                                <Input value={ this.state.price_rub } type="number" onChange={ this.handlePriceRubChange } />
                            </FormItem>
                            <FormItem>
                                <div style={ form.label }>Цена (в коинах)</div>
                                <Input value={ this.state.price_coins } type="number" onChange={ this.handlePriceCoinsChange } />
                            </FormItem>
                            <FormItem>
                                <div style={ form.label }>Фотографии</div>
                                <File
                                    size="l"
                                    before={<Icon24Camera />}
                                    multiple
                                    getRef={ this.fileInput }
                                    onChange={ this.handleFileChange }
                                />
                            </FormItem>
                            <FormItem>
                                { previews } 
                            </FormItem>
                            <FormItem style={{display: 'flex', justifyContent: 'center'}}>
                                <Button size="l" onClick={ this.handleSubmit }>
                                    Создать объявление
                                </Button>
                            </FormItem>
                        </FormLayout>
                    </Group>
                </Panel>
            </View>
        );
    }
}

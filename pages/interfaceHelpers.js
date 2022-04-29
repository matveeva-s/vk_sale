import Image from "next/image";
import coinIcon from "../styles/coin.svg";
import {coin, itemCard } from "../styles/common";
import logo from "../styles/logo.png";
import {Header, Avatar, InitialsAvatar, Link, SimpleCell} from "@vkontakte/vkui";
import { header } from '../styles/common';

const coinsPrice = (price) => {
    if (price) return (
        <div style={{ display: 'flex', alignItems: 'center' }}>
            <div>{ price }&nbsp;</div>
            <Image src={ coinIcon } style={ coin } />
        </div>
    )
}
const rubPrice = (price) => {
    if (price) {
        return <div>{price} рублей</div>
    }
}
export const getItemPrice = ({ price_rub, price_coins}) => {
    return (
        <div style={itemCard.price}>
            { price_rub && rubPrice(price_rub)}
            { price_rub && price_coins && <div>&nbsp;/&nbsp;</div>}
            { price_coins && coinsPrice(price_coins) }
        </div>
    )
}

export const getUserCard = (user) => {
    const userInitials = user.name.split(' ').map(i => i[0]).join('');
    const avatar = user.avatar ? (
        <Avatar size={36} src={ user.avatar }/>
    ) : (
        <InitialsAvatar size={36}>{userInitials}</InitialsAvatar>
    );
    return (
        <Link href={user.sys_url} target='_blank' style={{ flexGrow: 1 }}>
            <SimpleCell before={ avatar } style={{ float: 'right' }}>
                {user.name}
            </SimpleCell>
        </Link>
    )
}

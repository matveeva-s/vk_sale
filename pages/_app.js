import '../styles/globals.css';
import '../styles/detailed-page.css';
import '../styles/VKSans.css';
import {
    AdaptivityProvider,
    ConfigProvider,
    AppRoot,
    SplitLayout,
    SplitCol,
    ViewWidth,
    Group,
} from "@vkontakte/vkui";
import "@vkontakte/vkui/dist/vkui.css";
import Head from 'next/head'
import { GarageHeader } from './header';


function GarageApp({ Component, pageProps, user }) {
    return (
        <ConfigProvider platform="vkcom">
            <AdaptivityProvider hasMouse={true} viewWidth={ViewWidth.DESKTOP} deviceHasHover={true}>
                <AppRoot mode="Full">
                    <Head>
                        <meta
                            name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no, user-scalable=no, viewport-fit=cover"
                        />

                        <title>Барахолка</title>
                    </Head>
                    <SplitLayout style={ { minHeight: '100%' } }>
                        <SplitCol>
                            <Group mode="card">
                                <GarageHeader user={ user } />
                            </Group>
                            <div style={{ padding: '0 40px' }}>
                                <Component {...pageProps} />
                            </div>
                        </SplitCol>
                    </SplitLayout>
                </AppRoot>
            </AdaptivityProvider>
        </ConfigProvider>
    )
}

GarageApp.getInitialProps = async (context) => {
    const { cookies } = context.ctx.req;
    const strCookie = Object.keys(cookies).reduce((acc, cur) => {
        acc += `${cur}=${cookies[cur]}; `;
        return acc;
    }, '');
    const headers = { cookie: strCookie };
    const res = await fetch(process.env.DJANGO_HOST + '/users/me/', { headers });
    const json = await res.json()
    return { user: json?.[0] }
}


export default GarageApp

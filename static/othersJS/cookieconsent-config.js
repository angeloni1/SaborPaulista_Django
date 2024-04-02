import 'https://cdn.jsdelivr.net/gh/orestbida/cookieconsent@3.0.0/dist/cookieconsent.umd.js';


document.documentElement.classList.add('cc--light-funky');

CookieConsent.run({
    guiOptions: {
        consentModal: {
            layout: "box",
            position: "bottom left",
            equalWeightButtons: true,
            flipButtons: false
        },
        preferencesModal: {
            layout: "box",
            position: "right",
            equalWeightButtons: true,
            flipButtons: false
        }
    },
    categories: {
        necessary: {
            readOnly: true
        },
        functionality: {}
    },
    language: {
        default: "en",
        autoDetect: "browser",
        translations: {
            en: {
                consentModal: {
                    title: "Definições de Cookies",
                    description: "Este site utiliza cookies para melhorar sua experiência de navegação. Ao continuar, você concorda com o uso de cookies.",
                    acceptAllBtn: "Aceitar Todos",
                    acceptNecessaryBtn: "Rejeitar Todos",
                    showPreferencesBtn: "Gerenciar",
                    // footer: "<a href=\"#link\">Privacy Policy</a>\n<a href=\"#link\">Terms and conditions</a>"
                },
                preferencesModal: {
                    title: "Configurações de Privacidade",
                    acceptAllBtn: "Aceitar Todos",
                    acceptNecessaryBtn: "Rejeitar Todos",
                    savePreferencesBtn: "Salvar",
                    closeIconLabel: "Fechar",
                    serviceCounterLabel: "Service|Services",
                    sections: [
                        {
                            title: "Uso dos cookies",
                            description: "Os cookies são pequenos arquivos que ajudam o site a lembrar suas preferências e oferecer uma experiência personalizada."
                        },
                        {
                            title: "Cookies Obrigatórios <span class=\"pm__badge\">Sempre Habilitado</span>",
                            description: "Necessários para autenticação, segurança e gerenciamento de sessões, incluindo o uso do reCAPTCHA. Ao contrário dos cookies de terceiros, não exigem consentimento do usuário, pois são indispensáveis para fornecer os serviços online.",
                            linkedCategory: "necessary"
                        },
                        {
                            title: "Cookies de Funcionalidades",
                            description: "Cookies de terceiros, como o Google Analytics, monitoram o comportamento do usuário em um site, coletando dados como páginas visitadas e tempo de permanência. Fornecidos por empresas de análise, esses cookies visam melhorar a experiência do usuário e oferecer insights sobre o desempenho do site.",
                            linkedCategory: "functionality"
                        }
                    ]
                }
            }
        }
    }
});
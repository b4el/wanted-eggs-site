"""Gera o site estático do Wanted Eggs (GitHub Pages).

Edite CONTATO/RESPONSAVEL/ATUALIZADO abaixo e rode: python3 build.py
"""
import html

CONTATO = 'wantedeggs.app@gmail.com'
RESPONSAVEL = 'Gabriel'
ATUALIZADO = '23 de novembro de 2026'

CSS = """
:root{--bg:#0E0E12;--card:#17171D;--border:#2A2A33;--text:#F4F1EA;--muted:#A9A6B2;--accent:#FF8A1F;--gold:#FFC531}
@media (prefers-color-scheme: light){:root{--bg:#F7F4EE;--card:#FFFFFF;--border:#E6E0D4;--text:#1B1A1F;--muted:#5E5B66;--accent:#A84F00}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,sans-serif}
a{color:var(--accent)}
.wrap{max-width:760px;margin:0 auto;padding:28px 20px 64px}
header{display:flex;align-items:center;gap:12px;margin-bottom:28px;flex-wrap:wrap}
header img{width:44px;height:44px;border-radius:12px}
.brand{font-family:Anton,Impact,sans-serif;font-size:26px;letter-spacing:1px;text-decoration:none;color:var(--text);white-space:nowrap}
.brand span{color:var(--accent)}
nav{margin-left:auto;display:flex;gap:16px;font-size:14px}
nav a{text-decoration:none;color:var(--muted);white-space:nowrap}
@media (max-width:560px){nav{width:100%;margin-left:0}}
h1{font-family:Anton,Impact,sans-serif;font-weight:400;font-size:40px;letter-spacing:.5px;line-height:1.1;margin:8px 0 6px}
h2{font-size:19px;margin:34px 0 8px}
.updated{color:var(--muted);font-size:14px;margin-bottom:24px}
.box{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:18px 20px;margin:18px 0}
.box.accent{border-color:var(--accent)}
li{margin:4px 0}
table{width:100%;border-collapse:collapse;font-size:15px}
td,th{border-bottom:1px solid var(--border);padding:10px 8px;text-align:left;vertical-align:top}
th{color:var(--muted);font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:1px}
footer{margin-top:48px;color:var(--muted);font-size:13px;border-top:1px solid var(--border);padding-top:16px}
.hero{padding:24px 0 8px}
.hero p{font-size:18px;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:24px 0}
.cards .box{margin:0}
.cards b{display:block;margin-bottom:4px}
"""


def page(slug: str, title: str, body: str) -> None:
    doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Wanted Eggs</title>
<meta name="description" content="Wanted Eggs: segredos, glitches e builds de jogos descobertos e votados pela comunidade.">
<link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body><div class="wrap">
<header>
  <img src="icon.png" alt="">
  <a class="brand" href="./">WANTED <span>EGGS</span></a>
  <nav><a href="termos.html">Termos</a><a href="privacidade.html">Privacidade</a><a href="excluir-conta.html">Excluir conta</a></nav>
</header>
{body}
<footer>Wanted Eggs é um app de fãs, <b>não oficial</b>, sem afiliação com Rockstar Games, Take-Two, Activision, Microsoft, FromSoftware, Bandai Namco, CD PROJEKT ou qualquer outra desenvolvedora ou editora. Nomes de jogos são marcas de seus donos.<br>Contato: <a href="mailto:{CONTATO}">{CONTATO}</a></footer>
</div></body></html>
"""
    with open(f'{slug}.html', 'w', encoding='utf-8') as f:
        f.write(doc)


# ------------------------------------------------------------------ Início
page('index', 'Início', f"""
<section class="hero">
  <h1>Segredos, glitches e builds dos seus jogos</h1>
  <p>A comunidade descobre, envia e vota: o que é <b>real</b>, o que é <b>mito</b>, qual glitch ainda funciona e qual build está dominando a meta.</p>
</section>
<div class="cards">
  <div class="box"><b>🥚 Real ou Mito?</b>Segredos e easter eggs confirmados pelos votos da comunidade.</div>
  <div class="box"><b>🐛 Ainda funciona?</b>Glitches do modo história testados por quem joga.</div>
  <div class="box"><b>🔥 Meta</b>Builds com print, código para importar e hype da galera.</div>
  <div class="box"><b>⭐ Patentes</b>Suba de Novato a Procurado 5 Estrelas.</div>
</div>
<div class="box accent">O app está em fase de testes e chega primeiro ao Android. Quer testar antes? Escreva para <a href="mailto:{CONTATO}">{CONTATO}</a>.</div>
""")

# ------------------------------------------------------------------ Termos
page('termos', 'Termos de Uso', f"""
<h1>Termos de Uso</h1>
<div class="updated">Última atualização: {ATUALIZADO}</div>

<div class="box">Resumo: o Wanted Eggs é um app de fãs, gratuito e não oficial. Respeite as pessoas, poste só o que é seu, nada de trapaça online. Você é dono do que envia e nos autoriza a mostrar isso no app. Podemos remover conteúdo e contas que quebrem estas regras.</div>

<h2>1. O que é o Wanted Eggs</h2>
<p>O Wanted Eggs (“app”) é um aplicativo de comunidade para catalogar e votar em segredos (easter eggs), glitches e dicas/builds de jogos. É mantido por {RESPONSAVEL} (“nós”). O app é <b>não oficial</b> e não tem afiliação com as desenvolvedoras ou editoras dos jogos citados.</p>

<h2>2. Quem pode usar</h2>
<ul>
<li>Qualquer pessoa pode navegar e ler sem conta.</li>
<li>Para criar conta é preciso ter <b>pelo menos 13 anos</b>. Menores de 18 anos devem usar o app com o conhecimento e a autorização de seus pais ou responsáveis.</li>
<li>Uma pessoa, uma conta. Você é responsável pelo que acontece na sua conta e pelo acesso ao seu e-mail.</li>
</ul>

<h2>3. Regras da comunidade</h2>
<ul>
<li>Respeito: nada de ofensas, discurso de ódio, assédio, ameaças, conteúdo sexual ou violência real.</li>
<li>Poste só conteúdo seu: prints e textos feitos por você. Não copie textos, imagens, vídeos ou rankings de outros sites ou criadores.</li>
<li><b>Glitches só de modo história/offline.</b> É proibido postar trapaças, exploits ou glitches que deem vantagem no online, prejudiquem outros jogadores ou violem as regras dos jogos.</li>
<li>Nada de spam, propaganda, golpes, links maliciosos, venda de contas ou itens.</li>
<li>Não tente burlar votações, criar contas falsas ou atacar o app.</li>
<li>Não publique dados pessoais seus ou de outras pessoas.</li>
</ul>

<h2>4. O seu conteúdo</h2>
<p>Você continua dono do que envia (textos, prints, builds, comentários). Ao enviar, você nos dá uma licença gratuita, mundial e não exclusiva para exibir, armazenar, adaptar o formato (por exemplo, reduzir o tamanho da imagem) e divulgar esse conteúdo no app, no site e em materiais de divulgação do Wanted Eggs, enquanto ele estiver publicado. Você garante que tem o direito de enviar o conteúdo.</p>
<p>Os votos (“Real”, “Mito”, “Funciona”, hype) são da comunidade e podem mudar o status de um conteúdo. Não garantimos que informações enviadas pela comunidade sejam corretas.</p>

<h2>5. Moderação</h2>
<p>Qualquer pessoa pode denunciar conteúdo ou bloquear outro usuário. Podemos ocultar ou remover conteúdo e suspender ou encerrar contas que violem estes Termos ou a lei, com ou sem aviso prévio. Palavras ofensivas são bloqueadas automaticamente.</p>

<h2>6. Uso dos glitches e dicas por sua conta e risco</h2>
<p>Glitches, dicas e builds são compartilhados pela comunidade. Use por sua conta e risco: atualizações dos jogos podem corrigi-los, e o uso pode violar regras das desenvolvedoras. Não nos responsabilizamos por perda de progresso, banimentos ou outros problemas no seu jogo.</p>

<h2>7. Recursos pagos e anúncios</h2>
<p>O app é gratuito. No futuro poderá exibir anúncios e oferecer um plano premium (“Cinco Estrelas”), com selo e recursos extras. Quando existir, as condições de preço, renovação e cancelamento serão mostradas antes da compra, que será feita pela loja de aplicativos.</p>

<h2>8. Disponibilidade</h2>
<p>O app é oferecido “como está”. Podemos mudar, pausar ou encerrar funcionalidades. Faremos o possível para manter o serviço estável, mas não garantimos que ele estará sempre disponível ou livre de erros.</p>

<h2>9. Excluir sua conta</h2>
<p>Você pode excluir sua conta a qualquer momento em Perfil → Excluir conta, ou pedindo por e-mail. Veja o que acontece com seus dados na <a href="privacidade.html">Política de Privacidade</a>.</p>

<h2>10. Mudanças nestes Termos</h2>
<p>Podemos atualizar estes Termos. Mudanças importantes serão avisadas no app. Continuar usando o app depois da mudança significa que você concorda com a nova versão.</p>

<h2>11. Lei e foro</h2>
<p>Estes Termos seguem as leis do Brasil. Fica eleito o foro do domicílio do usuário consumidor, nos termos do Código de Defesa do Consumidor.</p>

<h2>12. Contato</h2>
<p><a href="mailto:{CONTATO}">{CONTATO}</a></p>
""")

# ------------------------------------------------------------------ Privacidade
page('privacidade', 'Política de Privacidade', f"""
<h1>Política de Privacidade</h1>
<div class="updated">Última atualização: {ATUALIZADO}</div>

<div class="box">Resumo: coletamos só o necessário para o app funcionar — seu e-mail para login, o nome e a foto que você escolhe e o que você posta. Não vendemos seus dados. Seus dados ficam em servidores no Brasil (São Paulo). Você pode excluir sua conta pelo app a qualquer momento.</div>

<h2>1. Quem cuida dos seus dados</h2>
<p>O controlador dos dados é {RESPONSAVEL}, responsável pelo Wanted Eggs. Contato do encarregado (DPO) para assuntos de privacidade: <a href="mailto:{CONTATO}">{CONTATO}</a>.</p>

<h2>2. Quais dados coletamos e por quê</h2>
<table>
<tr><th>Dado</th><th>Para quê</th><th>Base legal (LGPD)</th></tr>
<tr><td>E-mail</td><td>Login por código (sem senha) e contato sobre a sua conta</td><td>Execução do contrato</td></tr>
<tr><td>Nome de usuário e foto de perfil</td><td>Mostrar quem enviou, votou ou comentou</td><td>Execução do contrato</td></tr>
<tr><td>Conteúdo que você envia: segredos, glitches, dicas, builds, prints, comentários, sugestões de jogos</td><td>Publicar no app para a comunidade</td><td>Execução do contrato</td></tr>
<tr><td>Votos, hype, “achados”, bloqueios e denúncias</td><td>Funcionamento das votações, do seu checklist, da pontuação e da moderação</td><td>Execução do contrato e legítimo interesse (segurança da comunidade)</td></tr>
<tr><td>Dados técnicos: endereço IP, data e hora de acesso, tipo de aparelho</td><td>Segurança, prevenção de abuso e registro exigido pelo Marco Civil da Internet</td><td>Obrigação legal e legítimo interesse</td></tr>
</table>
<p><b>Fotos:</b> antes do envio, o próprio app reduz e regrava a imagem no seu aparelho, removendo metadados como a localização (GPS).</p>
<p>Não coletamos sua localização, contatos, senha de jogos ou dados de pagamento. Hoje o app não usa ferramentas de anúncio nem de rastreamento.</p>

<h2>3. Com quem compartilhamos</h2>
<ul>
<li><b>Supabase</b> (hospedagem do banco de dados, arquivos e login), com servidores na região de São Paulo, Brasil.</li>
<li><b>Google (Gmail)</b>, usado apenas para enviar o e-mail com o código de login.</li>
<li><b>Expo</b>, plataforma usada para construir e atualizar o app.</li>
<li>Autoridades, quando houver ordem judicial ou obrigação legal.</li>
</ul>
<p>O que você publica (nome de usuário, foto, posts, comentários) fica visível para qualquer pessoa no app. Seu e-mail nunca é mostrado a outros usuários.</p>
<p>Se no futuro passarmos a usar anúncios (ex.: Google AdMob) ou um plano premium (ex.: RevenueCat e lojas de aplicativos), esta política será atualizada antes, e pediremos seu consentimento quando a lei exigir.</p>

<h2>4. Por quanto tempo guardamos</h2>
<ul>
<li>Enquanto sua conta existir.</li>
<li>Ao excluir a conta: apagamos seu perfil, e-mail, foto, votos, achados, comentários, bloqueios, denúncias feitas por você e todas as imagens que você enviou. Segredos, glitches, dicas e sugestões de jogos que você publicou continuam no app <b>sem o seu nome</b> (anônimos), porque fazem parte do histórico da comunidade. Se quiser que algum deles seja apagado, peça por e-mail.</li>
<li>Registros de acesso (IP, data e hora) podem ser guardados por 6 meses, como exige o Marco Civil da Internet.</li>
</ul>

<h2>5. Seus direitos</h2>
<p>Pela LGPD você pode, a qualquer momento: confirmar se tratamos seus dados, acessá-los, corrigi-los (pelo app, em Perfil), pedir a exclusão, a portabilidade, informações sobre compartilhamento e revogar consentimentos. Para isso, escreva para <a href="mailto:{CONTATO}">{CONTATO}</a> a partir do e-mail da sua conta. Respondemos em até 15 dias. Você também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).</p>

<h2>6. Crianças e adolescentes</h2>
<p>O app não é destinado a menores de 13 anos e não permite que eles criem conta. Adolescentes entre 13 e 17 anos devem usar o app com o conhecimento e a autorização dos responsáveis. Se você souber de uma conta de menor de 13 anos, avise-nos que ela será excluída.</p>

<h2>7. Segurança</h2>
<p>Usamos conexão criptografada (HTTPS), controle de acesso por linha no banco de dados (cada pessoa só altera o que é seu), sessão guardada no armazenamento seguro do aparelho (Keychain/Keystore) e limites contra spam. Nenhum sistema é 100% seguro; se houver um incidente que traga risco a você, avisaremos.</p>

<h2>8. Mudanças nesta política</h2>
<p>Quando mudarmos esta política, atualizaremos a data acima e avisaremos no app se a mudança for importante.</p>

<h2>9. Contato</h2>
<p><a href="mailto:{CONTATO}">{CONTATO}</a></p>
""")

# ------------------------------------------------------------------ Excluir conta
page('excluir-conta', 'Excluir conta', f"""
<h1>Excluir sua conta</h1>
<div class="updated">Wanted Eggs</div>

<h2>Pelo app (na hora)</h2>
<ol>
<li>Abra o Wanted Eggs e entre na sua conta.</li>
<li>Toque em <b>Perfil</b>.</li>
<li>Toque em <b>Excluir conta</b> e confirme.</li>
</ol>

<h2>Sem o app (por e-mail)</h2>
<p>Se você já desinstalou o app, mande um e-mail para <a href="mailto:{CONTATO}?subject=Excluir%20minha%20conta%20Wanted%20Eggs">{CONTATO}</a> <b>a partir do e-mail da sua conta</b>, com o assunto “Excluir minha conta”. Excluímos em até 15 dias e confirmamos por e-mail.</p>

<h2>O que é apagado</h2>
<div class="box">
<ul>
<li><b>Apagado:</b> perfil, e-mail, foto, votos, achados, comentários, bloqueios, denúncias feitas por você e todas as imagens que você enviou.</li>
<li><b>Fica anônimo:</b> segredos, glitches, dicas e sugestões de jogos que você publicou continuam no app sem o seu nome. Se quiser que sejam apagados também, peça no mesmo e-mail.</li>
<li><b>Guardado por até 6 meses:</b> registros de acesso (IP, data e hora), por exigência do Marco Civil da Internet.</li>
</ul>
</div>
""")

print('ok')

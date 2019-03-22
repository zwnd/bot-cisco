#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot('salvecosta', 'Dusiklindo')

# Passar da forma que quiser, cada linha é um comentário
comentarios = [
     " @ahoratuyo_secondhand @umbrellacademy @denerxx",
 " @vargasjulia_ @penteadocaroline @yasmiimmr",
 " @rolneivinicios @poxa__day_ @thalitamaria__",
 " @lipeado @franciny_rosa @t.mincev",
 " @eduardaa__araujoo @moretti_c @williams.advocacia",
 " @nurulrahmania_ @v.allgayer @sinx_444",
 " @betocruz07 @sustodemoto @hallie_3585",
 " @sophia_paulah @_julianonathan @ficaquetalari",
 " @carolcomce_ @gustafsonbrenda @pamelaviviane",
 " @marcelochalegre @anaclara_boeno @alysonsanttos",
 " @veruskalucci @lanaa_subtil @bronxst",
 " @danyda_cruz @isbrlla @an4_live",
 " @biancaaborges_ @matheushermes3975 @cami_ramos2.0",
 " @wllvictor @marconi2909 @viih_ald953",
 " @keveencristian_21 @gicazuza @oianinha_",
 " @igorclaro @isascholl @tifansy",
 " @dedezao_ @lethall_lady @jennyjames1111",
 " @dayviannekarollinne @wirley_mont @sra.kleein",
 " @luhsoares2 @tchutcho_glizzy97 @leilane.m123",
 " @blognrollplay @jhobao_jb @vvvv_357",
 " @murphey.anne @kzayra @maduzou",
 " @yngrid_15_ @_saaaholiveira @_yasminbia_",
 " @radi0activ3_ @souzaxvr @giovanah_silvah",
 " @theidiots____ @deivid9987 @ana_araujot",
 " @raiissa_oliveiraa @suelenuai @bravusacai",
 " @nluciene45 @vihjustiniana @giiocezar",
 " @moniquemu7_ @luanarafaellaa @luhjaymc",
 " @russotdl777 @analu_meira @nagyla___loiola",
 " @alexsandraaraujo90 @renanalves.1.2 @va78oliveira",
 " @erick_ehbs @juliabragamaria @viih_ssz_",
 " @fehirooka @_danielprates_ @thaizeera",
 " @lorayneknupp @isabelam._ @sant0sandy",
 " @madu_.moraes @karool_001 @nattymeneses22",
 " @xmamedex @leonardosouza1231997 @lauracarol56",
 " @galmeeida_ @arielematoss @jeh_moreira_26",
 " @1995october @joelson_zime @mozachi_natalia",
 " @bronximports @brunozeos @cfbcjunior",
 " @italolcardoso @cardosopmatheus @euigxr",
 " @____wannessa_evellynh @menosprezzi @wagnerrabuski",
 " @rafaoliveira137 @profissaovender @joaovitor8354",
 " @_abimael_eliabe @thiele_jahnke @joao.lp_",
 " @batalhadovisconde @ttrezerecords @_bestnews_",
 " @sktbernardo @erik_marques31 @airaphaela",
 " @meninodoo7 @naah_osman @viana.dionatan",
 " @amandadias5856 @luan.27.k @anaavila97",
 " @cr.mec @jerrybatista_ @cdn.ruan",
 " @beladesouzaf @eduardogomes9983 @trx.16k",
 " @morganalvesdutra @rafaelmartinspe @ei.nunes",
 " @kauan.enderson @zibiastfny @keeey_ferraz",
 " @geovanna_dmc @ks_eletrostore @lihh_prado",
 " @eduuardohq @carlos_moreira92 @umclickparadicas",
 " @mariaedith2341 @mateu_zinho13 @davi.wesley1",
 " @3m3__santos @jheey_silva_ @rastalay",
 " @lunalemos05 @zeroh.memphis @prado_julian_",
 " @gomees32 @moraisthiago3105 @dan_arcanjoo",
 " @luccasmatheustf @edinhogomesjunior @larissa_cris13",
 " @esterdp_ @_tais1995 @jessy_scar",
 " @renato_goncalves_ @taylon_martins_ @ronaldmendes01",
 " @vinicius_primolan @_l3za @johnnymaks22",
 " @picstrust @talourenco_ @70_sorte",
 " @thalles.n15 @mariolliuminati @gabriel_geneski",
 " @grazieleferreirazinha2005 @nekinhan @leozinhomartins_",
 " @marinasiilvaii @gaby_ves @mandaa_1999",
 " @mariasantos9371 @dan.crf123456789 @dudaemts.me",
 " @felipeluiz._ @eujuliana_aguiar @matheus2004_",
 " @loucura28 @matheus_silva0016 @maria4575silva",
 " @harif_qusairry @agustin_skateco @leonardosouza6873",
 " @paulagleisy.rodrigues @lauanyleticiadaconceicaoso @allves_mariah_",
 " @pablojunior5881 @ketlenlk @cristianeferreiradasilva34",
 " @pedro.pablo.rds @aryanexantunes @ingrid_zd",
 " @franklinjohn_07 @britorh_ @pedro.csilva19",
 " @sophia_lima_malagueta @yonara_victoria @guilhermesilva8996",
 " @anabelenbussonn @queltonassi @geovana.alvesnascimento.16",
 " @f3rrazzz @prince1salvatore98 @lucianarillary",
 " @annalima300 @diegosouza3129 @amin.8176",
 " @yasminstoklein @sdl_bryk @_lariss_p",
 " @brunobraz_e_guilherme @joscleide_fernandes_da_costa @silvadjronny",
 " @kaducerqueira1 @marlonmatheusdasilva @gustavoribeiro568",
 " @brenda_silvaah__ @rikmm7 @dudas38",
 " @f.elisbertob @andreviniciiuss @_gavinharrison_",
 " @marsholc @santosalanaaa @naathcarol",
 " @palazzolli_ @xoxo.luluz @roniely_santana",
 " @_breviana @talivieir @kalitalitter",
 " @oliveiraav @isador4zz @onwnabe",
 " @carolanaconi @rhfler @o_almeidinha_",
 " @sesilva1 @halliday.ian @ana.farias1870",
 " @jgsantoos1 @gabrielvazzzzz @murassakiana",
 " @rickmorbeck @mateus.m367 @yung_guapingz",
 " @staygoldsb @ro_salviano @_lualmd",
 " @gabinogueira.sj @viyzz @andersonsena_",
 " @rcopat @x.x.x_i.c.ebig @cordanoitee",
 " @leilamrcastro @annacarln_ @cazuzaskate",
 " @gabirll @brunosmariano @viccrz_",
 " @julia_carvalho10 @gabyzinhaaa__ @lerinamariana",

]
for comentario in comentarios:
    bot.comment("1997525330202404384_8341157362", comentario)

# chama isso aqui no browser: https://www.instagram.com/publicapi/oembed/?callback=&url=AQUI A URL QUE TU QUER
# Exemplo: https://www.instagram.com/publicapi/oembed/?callback=&url=https://www.instagram.com/p/BucUdXSlEp3/
# procura por um media_ID parecido com isso: 1992337216253488658_367386260 e cola no "id do post"
# abre o terminal e procura a pasta que ta esse arquivo, Exemplo: cd desktop/bot-insta depois escreve pip install instapy e depois aperta f5



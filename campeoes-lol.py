def lower(listName):
    for i in range(len(listName)):
        listName[i] = listName[i].lower()

def main():

    #LISTS
    melhores = ['Akali', 'Brand', 'Diana', 'Garen','Karma', 'Lucian', 'Leblanc', 'Leona', 'Jinx',
                'Evelynn', 'Nami', 'Nautilus', 'Renata', 'Renata Glasc', 'Rengar', 'Soraka', 'Vayne', 'Veigar',
                'Vex', 'Xerath', 'Yuumi', 'Zed', 'Zeri']

    lower(melhores)

    lacre = ['Ahri', 'Annie', 'Ashe', "Bel'Veth", 'Belveth', 'Bel Veth', 'Cait', 'Caitlyn', 'Corki', 'Elise', 'Ez', 'Ezreal', 'Graves', 'Gwen',
             'Illaoi', 'Janna', 'Kaisa', "Kai'sa", 'Katarina', 'Kindred', 'Lillia', 'Lissandra', 'Lulu', 'MF', 'Miss Fortune',
             'Morgana', 'Neeko', 'Nidalee', 'Orianna', 'Poppy', 'Qiyana', 'Rakan', 'Rell', 'Senna', 'Seraphine', 'Sivir', 'Sona',
             'Syndra', 'Taliyah', 'Taric', 'Varus', 'Vi', 'Zoe', 'Zyra']

    lower(lacre)

    heterotop = ['Akshan', 'Alistar', 'Blitz', 'Blitzcrank', 'Braum', 'Camille', 'Cassiopeia', 'Darius', 'Draven', 'Ekko',
              'Fiddle', 'Fiddlesticks', 'Fiora', 'Fizz', 'Gnar', 'Gragas', 'Hecarim','Irelia', 'Jarvan IV',
              'Jarvan 4', 'Jax', 'Jayce', 'Jhin', 'Karthus', 'Kassadin', 'Kayle', 'Kayn', 'Khazix', "Kha'Zix" 'Kled', 'Kog',
              "Kog'Maw", 'Master', 'Master Yi', 'Nasus', 'Noc', 'Nocturne','Olaf', 'Pantheon', 'Pyke',
              'Quinn', 'Renekton', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sett', 'Shaco', 'Sylas', 'Talon', 'Teemo', 'Thresh',
              'Tristana', 'Trynda', 'Tryndamere', 'TF', 'Twisted Fate', 'Twitch', 'Velkoz', "Vel'Koz", 'Viego', 'Viktor',
              'Vlad', 'Vladimir', 'Xayah', 'Xin Zhao', 'Yasuo', 'Yone', 'Ziggs']

    lower(heterotop)

    esquecidos = ['Aatrox', 'Amumu', 'Anivia', 'Aphelios', 'Aurelion', 'Aurelion Sol', 'Azir', 'Bardo', 'Cho', "Cho'gath", 'Dr Mundo', 'Mundo',
                  'Galio','Heimerdinger', 'Ivern', 'Kalista', 'Kennen', 'Malzahar', 'Maokai', 'Mordekaiser', 'Nunu', 'Ornn',
                  'Rammus', 'Rek', 'Reksai', "Rek'Sai", 'Sejuani', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Skarner', 'Swain', 'Tahm Kench', 'Trundle',
                  'Udyr', 'Urgot', 'Volibear', 'Warwick', 'Yorick', 'Zac', 'Zilean']

    lower(esquecidos)

    kibas = ['Lee', 'Lee Sin', 'LeeSin', 'Barril', 'GP', 'Gepeto', 'Gangplank', 'Pedra', 'Malpito', 'Malphite']

    lower(kibas)

    #INPUT
    userChamp = str(input('Fala um champ bom: ')).lower()

    # IF ELSE STATEMENTS
    if userChamp in melhores:
        print('VC TEM ÓTIMO GOSTO')
    elif userChamp in lacre:
        print('lacrou mana')
    elif userChamp in heterotop:
        print('calado verdinho!!!')
    elif userChamp in kibas:
        print('EBA, VOCÊ É O KIBAS <3')
    elif userChamp == 'Lux'.lower():
        print('Parabéns, você conseguiu falar o único campeão que tem uma categoria especial SÓ PRA XINGAR, SUA COISA HORRENDA!!! #LUXHATERS')
    elif userChamp in esquecidos:
        print('Eu falei um champ bom KKKKKKKKKKK')
    else:
        print('Fala um champ, caramba')

#REPEATING GAME
def end():

    yes = ['Sim', 'S']
    lower(yes)

    no = ['Não', 'Nao', 'N']
    lower(no)

    question = str(input('Quer jogar de novo? ')).lower()

    while True:
        if question in yes:
            main()
            end()
        elif question in no:
            break
        else:
            print('Escreve direito alienigena')
            end()

#EXEC

main()
end()
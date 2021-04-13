import unittest
import random
from solution import Trie, enemy_revealer
from collections import defaultdict
from typing import List


class TestCodingChallenge10(unittest.TestCase):
    def build_trie(self, trie: Trie, enemies: List[str]) -> None:
        for enemy in enemies:
            trie.insert(enemy)

    def test_single_words(self):
        test = ["Angel", "Banshee", "Basilisk", "ChaosBug", "Corpse"]
        trie = Trie()
        self.build_trie(trie, test)

        expected = ["Angel"]
        actual = enemy_revealer(trie, "A")
        self.assertCountEqual(expected, actual)

        expected = ["Banshee", "Basilisk"]
        actual = enemy_revealer(trie, "B")
        self.assertCountEqual(expected, actual)

        expected = ["Corpse"]
        actual = enemy_revealer(trie, "C")
        self.assertCountEqual(expected, actual)

        # Should only return 'Banshee'!
        expected = ["Banshee"]
        actual = enemy_revealer(trie, "Bansh")
        self.assertCountEqual(expected, actual)

        # Should return nothing!
        expected = []
        actual = enemy_revealer(trie, "Chaos")
        self.assertCountEqual(expected, actual)

    def test_prefixes(self):
        test = ["Banshee", "BerenikeKnight", "BlackKnight", "Butcher", "BoneWheel"]
        trie = Trie()
        self.build_trie(trie, test)

        expected = ["BoneWheel"]
        actual = enemy_revealer(trie, "BW")
        self.assertCountEqual(expected, actual)

        expected = ["Butcher"]
        actual = enemy_revealer(trie, "Bu")
        self.assertCountEqual(expected, actual)

        # Should return both of the knights
        expected = ["BerenikeKnight", "BlackKnight"]
        actual = enemy_revealer(trie, "BKn")
        self.assertCountEqual(expected, actual)

        # Should only return 'BerenikeKnight'!
        # The 'BlackKnight' is not prefixed with 'Be'
        expected = ["BerenikeKnight"]
        actual = enemy_revealer(trie, "BeKn")
        self.assertCountEqual(expected, actual)

        # Should return nothing!\
        expected = []
        actual = enemy_revealer(trie, "BKing")
        self.assertCountEqual(expected, actual)

        # Enemies that are three words
        # Should return nothing!
        expected = []
        actual = enemy_revealer(trie, "BeKT")
        self.assertCountEqual(expected, actual)

    def test_basic(self):
        test = ['DancerOfTheBorealValley', 'DarkSunGwyndolin', 'DarkeaterMidir',
                'DarkmoonSoldiers', 'Darkwraith', 'DarkwraithKnight',
                'DaughterOfCrystalKriemhild', 'Deacon', 'DeaconsOfTheDeep',
                'DeepAccursed', 'Demon', 'DemonCleric', 'DemonFiresage',
                'DemonFromBelow', 'DemonInPain', 'DemonPrince', 'DemonStatue',
                'DesertPyromancerZoey', 'DevoutHollow', 'DragonslayerArmour', 'Drake',
                'DrakebloodKnight', 'DrangKnights']
        trie = Trie()
        self.build_trie(trie, test)

        # 'Deacon' and 'Drake' appear because 'a' is present in each of those words
        expected = ['Darkwraith', 'Deacon', 'Drake']
        actual = enemy_revealer(trie, "Da")
        self.assertCountEqual(expected, actual)

        expected = ['DarkwraithKnight', 'DrakebloodKnight', 'DrangKnights']
        actual = enemy_revealer(trie, "DrK")
        self.assertCountEqual(expected, actual)

        # Handle 4 words
        expected = ['DaughterOfCrystalKriemhild']
        actual = enemy_revealer(trie, "DOCystK")
        self.assertCountEqual(expected, actual)

        test = ['SagesPrentice', 'Scholar', 'SeathTheScaleless', 'Sentinel',
                'SerpentMage', 'SewerCentipede', 'ShiraKnightOfFilianore', 'SilverKnight',
                'SirVilhelm', 'SisterFriede', 'Skeleton', 'SkeletonBaby', 'SkeletonBall',
                'SkeletonBeast', 'SkeletonWheel', 'SlaveKnightGael', 'Slime',
                'SmallMushroomPeople', 'SmallRats', 'SmoulderingFlesh', 'SnowRat',
                'StarvedHound', 'StoneDemon', 'StoneGuardian', 'StrayDemon',
                'SulyvahnsBeast', 'SurvivorOfTheFlame', 'SwordMaster'
                ]
        trie = Trie()
        self.build_trie(trie, test)

        expected = ['SkeletonBaby', 'SkeletonBall', 'SkeletonBeast']
        actual = enemy_revealer(trie, "SkelB")
        self.assertCountEqual(expected, actual)

        expected = ['StoneDemon', 'StrayDemon']
        actual = enemy_revealer(trie, "SDemon")
        self.assertCountEqual(expected, actual)

        expected = ['SmallRats', 'SnowRat']
        actual = enemy_revealer(trie, "SR")
        self.assertCountEqual(expected, actual)

        expected = ['ShiraKnightOfFilianore']
        actual = enemy_revealer(trie, "ShiraKnightOfFilianore")
        self.assertCountEqual(expected, actual)

    def test_comprehensive(self):
        test = [
            'AbyssWatchers', 'AldrichDevourerOfGods', 'AncientWyvern', 'Angel', 'AngelPilgrim',
            'AsylumDemon', 'BalderKnight',
            'Banshee', 'Basilisk', 'BatWingDemon', 'BellGargoyle', 'BlackHandKamui', 'BlackKnight',
            'BlowdartSniper',
            'BlueLothricKnight', 'BoneTower', 'BorealOutriderKnight', 'BoundingDemonOfIzalith',
            'Brigand', 'BurrowingRockworm',
            'CagedHollow', 'CapraDemon', 'CarthusGraveWarden', 'CarthusSandworm',
            'CarthusSwordsman', 'CathedralGraveWarden',
            'CathedralKnight', 'CeaselessDischarge', 'CentipedeDemon', 'ChainedPrisoner',
            'ChampionGundyr',
            'ChampionsGravetender', 'ChaosBug', 'ChaosEater', 'ChaosWitchQuelaag', 'Corpse',
            'Corvian', 'CorvianKnight',
            'CorvianSettler', 'CorvianStoryteller', 'CourtSorcerer', 'Crab', 'Cragspider',
            'CrossbreedPriscilla', 'CrowDemon',
            'CrystalGolem', 'CrystalKnight', 'CrystalLizard', 'CrystalSage', 'CurseRottedGreatwood',
            'DancerOfTheBorealValley',
            'DarkSunGwyndolin', 'DarkeaterMidir', 'DarkmoonSoldiers', 'Darkwraith',
            'DarkwraithKnight',
            'DaughterOfCrystalKriemhild', 'Deacon', 'DeaconsOfTheDeep', 'DeepAccursed', 'Demon',
            'DemonCleric', 'DemonFiresage',
            'DemonFromBelow', 'DemonInPain', 'DemonPrince', 'DemonStatue', 'DesertPyromancerZoey',
            'DevoutHollow',
            'DragonslayerArmour', 'Drake', 'DrakebloodKnight', 'DrangKnights', 'EggCarrier',
            'ElderGhru', 'EliteHollowSoldier',
            'EngorgedHollow', 'Ents', 'Evangelist', 'FallenKnight', 'FarronFollower', 'FireWitch',
            'FlamingAttackDog',
            'FleshOfAldrich', 'ForestProtectors', 'FourKings', 'Frogray', 'GapingDragon',
            'Gargoyle', 'GertrudesKnight', 'Ghost',
            'GhruConjurator', 'GhruGrunt', 'GhruLeaper', 'Giant', 'GiantCrab', 'GiantFly',
            'GiantHumanity', 'GiantLeech',
            'GiantManserpent', 'GiantMosquito', 'GiantOfTheUndeadSettlement', 'GiantRat',
            'GiantSkeleton', 'GiantSkeletonArcher',
            'GraveWarden', 'GravetenderGreatwolf', 'GreatFeline', 'GreatGreyWolfSif',
            'GreatStoneKnight', 'GwynLordOfCinder',
            'HalflightSpearOfTheChurch', 'HaraldKnight', 'HavelKnight', 'HeadlessGargoyle',
            'HighLordWolnir', 'Hollow',
            'HollowAssassin', 'HollowCleric', 'HollowManservant', 'HollowPriest', 'HollowSoldier',
            'HollowWarrior',
            'IcyGiantCrab', 'InfestedBarbarian', 'InfestedCorpse', 'InfestedGhoul',
            'IrithyllianHound', 'IrithyllianSlave',
            'IronDragonslayer', 'IronGolem', 'IudexGundyr', 'Jailer', 'JailerHollow', 'Judicator',
            'KingOfTheStorm',
            'KnightSlayerTsorig', 'LargeMushroomPeople', 'LargeRats', 'LionKnightAlbert',
            'LocustPreacher', 'LothricKnight',
            'LothricWyvern', 'Lycanthrope', 'LycanthropeHunter', 'MadGhru', 'Madwoman',
            'Maggotgrub', 'ManSerpent',
            'ManeaterShell', 'Mangrub', 'Manserpent', 'ManserpentSummoner', 'MassOfSouls',
            'MillwoodKnight', 'Mimic',
            'MinorCapraDemon', 'MinorMoonlightButterfly', 'MinorTaurusDemon', 'MonstrosityOfSin',
            'MoonlightButterfly',
            'Murkman', 'NamelessKing', 'Necromancer', 'Nito', 'OceirosTheConsumedKing',
            'OldDemonKing', 'OolacileResident',
            'OolacileSorceress', 'OrnsteinAndSmough', 'OscarOfAstora', 'OutriderKnight',
            'OvergrownLothricKnight',
            'PaintingGuardian', 'ParasiticWallHugger', 'Phalanx', 'Pinwheel', 'PinwheelServant',
            'Pisaca', 'PoisonhornBug',
            'PontiffKnight', 'PontiffSulyvahn', 'PossessedTree', 'PusOfMan', 'RapierChampion',
            'Rat', 'RavenousCrystalLizard',
            'ReanimatedCorpse', 'RingedCityHollow', 'RingedKnight', 'RockLizard', 'RootSkeleton',
            'RottenFlesh', 'RottenSlug',
            'RoyalSentinel', 'SagesPrentice', 'Scholar', 'SeathTheScaleless', 'Sentinel',
            'SerpentMage', 'SewerCentipede',
            'ShiraKnightOfFilianore', 'SilverKnight', 'SirVilhelm', 'SisterFriede', 'Skeleton',
            'SkeletonBaby', 'SkeletonBall',
            'SkeletonBeast', 'SkeletonWheel', 'SlaveKnightGael', 'Slime', 'SmallMushroomPeople',
            'SmallRats',
            'SmoulderingFlesh', 'SnowRat', 'StarvedHound', 'StoneDemon', 'StoneGuardian',
            'StrayDemon', 'SulyvahnsBeast',
            'SurvivorOfTheFlame', 'SwordMaster', 'TaurusDemon', 'TheBedOfChaos', 'TheChanneler',
            'Thrall', 'TorchHollows',
            'TreantGardener', 'TreeLizard', 'TreeWoman', 'TwinExiles', 'TwinPrinces',
            'UndeadAssassin', 'UndeadAttackDog',
            'UndeadCrystalArcher', 'UndeadCrystalSoldier', 'UndeadKnightArcher', 'UndeadSoldier',
            'Vagrants', 'VileMaggot',
            'VordtOfTheBorealValley', 'WheelSkeleton', 'WildDog', 'WingedKnight', 'Wisp', 'Wolf',
            'WorkerHollow', 'Wretch',
            'Wyvern', 'YhormTheGiant'
        ]
        trie = Trie()
        self.build_trie(trie, test)

        expected = ['Corpse', 'Corvian', 'Crab', 'Cragspider']
        actual = enemy_revealer(trie, "C")
        self.assertCountEqual(expected, actual)

        expected = ['Jailer', 'Judicator']
        actual = enemy_revealer(trie, "J")
        self.assertCountEqual(expected, actual)

        expected = ['Necromancer', 'Nito']
        actual = enemy_revealer(trie, "N")
        self.assertCountEqual(expected, actual)

        expected = ['Madwoman', 'Mangrub', 'Manserpent', 'Murkman']
        actual = enemy_revealer(trie, "Man")
        self.assertCountEqual(expected, actual)

        expected = ['MassOfSouls', 'MonstrosityOfSin']
        actual = enemy_revealer(trie, "MOfS")
        self.assertCountEqual(expected, actual)

        expected = ['OvergrownLothricKnight']
        actual = enemy_revealer(trie, "OLKnight")
        self.assertCountEqual(expected, actual)

        expected = ['GravetenderGreatwolf']
        actual = enemy_revealer(trie, "GavetdrGrtf")
        self.assertCountEqual(expected, actual)

        test = ['Banshee', 'Beaconsofthedeep', 'Bourkings',
                'Browdemon', 'Bontiffknight', 'Brithyllianslave', 'Bheelskeleton',
                'Badghru', 'Baggotgrub', 'Biantfly', 'Boisonhornbug', 'Bhaoseater',
                'Biantskeletonarcher', 'Bocklizard', 'Bncientwyvern', 'Bothricknight',
                'Bingofthestorm', 'Breatstoneknight', 'Bragspider', 'Bhalanx', 'Busofman',
                'Bndeadknightarcher', 'Brystalsage', 'Bingedknight', 'Brakebloodknight',
                'Blaveknightgael', 'Bingedcityhollow', 'Bkeleton', 'Bargemushroompeople',
                'Blderghru', 'Bggcarrier', 'Bndeadcrystalsoldier', 'Borestprotectors',
                'Blackhandkamui', 'Btraydemon', 'Boundingdemonofizalith', 'Bhebedofchaos',
                'Baughterofcrystalkriemhild', 'Btarvedhound', 'Bottenslug', 'Borpse',
                'Banserpent', 'Bvergrownlothricknight', 'Bourtsorcerer', 'Bndeadassassin',
                'Birewitch', 'Barksungwyndolin', 'Bemonprince', 'Bagedhollow',
                'Bemoninpain', 'Blddemonking', 'Bilverknight', 'Bemonstatue',
                'Barkmoonsoldiers', 'Barthussandworm', 'Baintingguardian', 'Breelizard',
                'Bemonfiresage', 'Bocustpreacher', 'Bycanthrope', 'Bolacileresident',
                'Bamelessking', 'Bonetower', 'Bluelothricknight', 'Bhost', 'Bngelpilgrim',
                'Bordtoftheborealvalley', 'Bretch', 'Bhechanneler', 'Bhruconjurator',
                'Bollow', 'Baprademon', 'Bolacilesorceress', 'Bcholar', 'Bapingdragon',
                'Brogray', 'Bnts', 'Bighlordwolnir', 'Bontiffsulyvahn',
                'Boonlightbutterfly', 'Bewercentipede', 'Borvian', 'Bemonfrombelow',
                'Borkerhollow', 'Boyalsentinel', 'Biantcrab', 'Bldrichdevourerofgods',
                'Brossbreedpriscilla', 'Bndeadcrystalarcher', 'Bhainedprisoner']
        trie = Trie()
        self.build_trie(trie, test)

        actual = enemy_revealer(trie, "B")
        self.assertCountEqual(test, actual)

        expected = ['Banshee', 'Banserpent', 'Bagedhollow', 'Bargemushroompeople',
                    'Barkmoonsoldiers', 'Baughterofcrystalkriemhild', 'Bamelessking',
                    'Baprademon', 'Beaconsofthedeep', 'Bemonstatue', 'Bemonfiresage',
                    'Bocustpreacher', 'Bordtoftheborealvalley', 'Bolacileresident',
                    'Bolacilesorceress', 'Boyalsentinel', 'Brithyllianslave',
                    'Breatstoneknight', 'Bragspider', 'Brakebloodknight', 'Brystalsage',
                    'Bhechanneler', 'Bhaoseater', 'Bhainedprisoner', 'Biantskeletonarcher',
                    'Bndeadknightarcher', 'Bndeadcrystalsoldier', 'Bndeadcrystalarcher',
                    'Blaveknightgael', 'Bggcarrier', 'Btraydemon', 'Btarvedhound',
                    'Bycanthrope'
                    ]
        actual = enemy_revealer(trie, "Bae")
        self.assertCountEqual(expected, actual)

        expected = ['Bontiffknight', 'Bothricknight', 'Breatstoneknight',
                    'Brakebloodknight', 'Bingedknight', 'Bilverknight', 'Bndeadknightarcher',
                    'Blaveknightgael', 'Bluelothricknight', 'Bvergrownlothricknight']
        actual = enemy_revealer(trie, "Bknight")
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

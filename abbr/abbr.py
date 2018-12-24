# Copyright 2016 Adler Brediks Medrado
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from importlib import import_module

from abbr.exceptions import (
    LengthNotFoundError,
    LengthSizeError,
    LanguageNotFoundError,
    PhraseNotFoundError
)


class Abbreviate:
    def __init__(self, phrase, length, language):
        self.phrase = phrase
        self.length = length
        self.language = language
        self.new_phrase = phrase

    def do_abbreviation(self):
        dictionary = import_module(
            "abbr.languages.{}.dictionary".format(self.language)
        )
        for key, value in dictionary.word_list.items():
            self.new_phrase = self.new_phrase.replace(key, value)

    def truncate_phrase(self):
        self.new_phrase = self.new_phrase[:self.length]

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length == '':
            raise LengthNotFoundError('Length cannot be empty')
        if length == 0:
            raise LengthSizeError('Length must be greater then zero')

        self.__length = length

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if len(language.strip()) == 0:
            raise LanguageNotFoundError('Language cannot be empty')

        self.__language = language

    @property
    def phrase(self):
        return self.__phrase

    @phrase.setter
    def phrase(self, phrase):
        if len(phrase.strip()) == 0:
            raise PhraseNotFoundError('Phrase cannot be empty')

        self.__phrase = phrase

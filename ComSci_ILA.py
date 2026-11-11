{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO4QREO5alYKS7pkaAt1nVe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Philipissogwapo/Q2_Assesments_Narra/blob/ILA/ComSci_ILA.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "njFtYYjATsPX",
        "outputId": "75772ab2-d663-4cba-b2d0-5741c1d51ccc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "---The Guessing Game---\n",
            "\n",
            "The goal of the game is to guess a number between 1-100. No hints. You have five guesses.\n",
            "\n",
            "Your first guess : 17\n",
            "\n",
            "Wow! You got it in one guess! Congratulations.\n",
            "\n",
            "---End of Game---\n"
          ]
        }
      ],
      "source": [
        "def guessinggame():\n",
        "\n",
        "  secretnumber = 17\n",
        "  guessedcorrectly = False\n",
        "\n",
        "  print(\"---The Guessing Game---\\n\")\n",
        "  print(\"The goal of the game is to guess a number between 1-100. No hints. You have five guesses.\")\n",
        "\n",
        "  while True:\n",
        "    try:\n",
        "      userinput1 = int(input(\"\\nYour first guess : \"))\n",
        "\n",
        "      if userinput1 < 0:\n",
        "        continue\n",
        "      elif userinput1 > secretnumber or userinput1 < secretnumber:\n",
        "        print(\"\\nThat is not correct, you have 4 more tries.\")\n",
        "        break\n",
        "      else:\n",
        "        print(\"\\nWow! You got it in one guess! Congratulations.\")\n",
        "        guessedcorrectly = True\n",
        "        break\n",
        "    except ValueError:\n",
        "      print(\"\\nYou can only input integers. Try again.\")\n",
        "\n",
        "  while not guessedcorrectly:\n",
        "    try:\n",
        "      userinput2 = int(input(\"\\nYour second guess : \"))\n",
        "\n",
        "      if userinput2 < 0:\n",
        "        continue\n",
        "      elif userinput2 > secretnumber or userinput2 < secretnumber:\n",
        "        print(\"\\nThat's fine you can still guess it. You have 3 more tries.\")\n",
        "        break\n",
        "      else:\n",
        "        print(\"\\nYou only needed two guesses? Nice.\")\n",
        "        guessedcorrectly = True\n",
        "        break\n",
        "    except ValueError:\n",
        "      print(\"\\nYou can only input integers. Try again.\")\n",
        "\n",
        "  while not guessedcorrectly:\n",
        "    try:\n",
        "      userinput3 = int(input(\"\\nYour third guess : \"))\n",
        "\n",
        "      if userinput3 < 0:\n",
        "        continue\n",
        "      elif userinput3 > secretnumber or userinput3 < secretnumber:\n",
        "        print(\"\\nI believe in you. You have 2 more tries.\")\n",
        "        break\n",
        "      else:\n",
        "        print(\"\\nYou're incredibly lucky! You got it in 3 tries.\")\n",
        "        guessedcorrectly = True\n",
        "        break\n",
        "    except ValueError:\n",
        "      print(\"\\nYou can only input integers. Try again.\")\n",
        "\n",
        "\n",
        "  while not guessedcorrectly:\n",
        "    try:\n",
        "      userinput4 = int(input(\"\\nYour fourth guess : \"))\n",
        "\n",
        "      if userinput4 < 0:\n",
        "        continue\n",
        "      elif userinput4 > secretnumber or userinput4 < secretnumber:\n",
        "        print(\"\\nCome on, you can do this. You have 1 more try.\")\n",
        "        break\n",
        "      else:\n",
        "        print(\"\\nJust safe! You got it in 4 tries.\")\n",
        "        guessedcorrectly = True\n",
        "        break\n",
        "    except ValueError:\n",
        "      print(\"\\nYou can only input integers. Try again.\")\n",
        "\n",
        "  while not guessedcorrectly:\n",
        "    try:\n",
        "      userinput5 = int(input(\"\\nYour last guess : \"))\n",
        "\n",
        "      if userinput5 < 0:\n",
        "        continue\n",
        "      elif userinput5 > secretnumber or userinput5 < secretnumber:\n",
        "        print(\"\\nYou lost, the secret number is 17.\")\n",
        "        break\n",
        "      else:\n",
        "        print(\"\\nNice! You won with the last guess! Good job.\")\n",
        "        guessedcorrectly = True\n",
        "        break\n",
        "    except ValueError:\n",
        "      print(\"\\nYou can only input integers. Try again.\")\n",
        "\n",
        "  print(\"\\n---End of Game---\")\n",
        "\n",
        "guessinggame()"
      ]
    }
  ]
}
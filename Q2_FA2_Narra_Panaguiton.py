{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOTfiw9JtlpPpZqZeJe39Np",
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
        "<a href=\"https://colab.research.google.com/github/Philipissogwapo/Q2_Assesments_Narra/blob/ILA/Q2_FA2_Narra_Panaguiton.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sum of Numbers Using a For Loop**"
      ],
      "metadata": {
        "id": "w7Hrd4dG8oJH"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2Mo0ZWb76yRd",
        "outputId": "feac187f-8a8e-4ad6-b2ea-431901d94107"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "---Sum of Numbers---\n",
            "\n",
            "What is your age? : 6\n",
            "\n",
            "Expected sum is 447.\n",
            "\n",
            "Validating the sum using a validation checker...\n",
            "\n",
            "The sum is 21.0.\n",
            "\n",
            "Output invalid.\n"
          ]
        }
      ],
      "source": [
        "def getSum(number):\n",
        "  for i in range(number):\n",
        "    number += number + 1\n",
        "  return number\n",
        "\n",
        "def verifier(number):\n",
        "  sum = number * (number + 1) / 2\n",
        "  return sum\n",
        "\n",
        "print(\"---Sum of Numbers---\\n\")\n",
        "\n",
        "while True:\n",
        "  try:\n",
        "    number = int(input(\"What is your age? : \"))\n",
        "    break\n",
        "\n",
        "    if number < 0:\n",
        "      print(\"\\nNumbers below 0 are not allowed. Try again.\")\n",
        "      continue\n",
        "\n",
        "  except ValueError:\n",
        "    print(\"\\nYou cannot put that, try again.\")\n",
        "\n",
        "getSum = getSum(number)\n",
        "verifier = verifier(number)\n",
        "\n",
        "print(f\"\\nExpected sum is {getSum}.\")\n",
        "print(f\"\\nValidating the sum using a validation checker...\")\n",
        "print(f\"\\nThe sum is {verifier}.\")\n",
        "\n",
        "if getSum == verifier:\n",
        "  print(\"\\nOutput verified.\")\n",
        "else:\n",
        "  print(\"\\nOutput invalid.\")\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}
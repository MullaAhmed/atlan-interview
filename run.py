# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class RatingResponse(Resource):

    def get(self):
        message = {
    "_items": [
      {
        "answers": [
          {
            "text": "Pk",
            "questionId": "5K6D6rtUtF",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "txt",
            "questionTitle": "Name",
            "questionAlias": "name"
          },
          {
            "text": "fhkdnzoz",
            "questionId": "dyhi1I24WD",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "not",
            "questionTitle": "Note",
            "questionAlias": "note"
          },
          {
            "text": "a@b.com",
            "questionId": "LmGvZ7O5dx",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "ema",
            "questionTitle": "Email",
            "questionAlias": "email"
          },
          {
            "text": "Male",
            "questionId": "vUEexXhWNS",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "mcq",
            "questionTitle": "Gender",
            "questionAlias": "gender"
          },
          {
            "text": "22",
            "number": 22,
            "questionId": "WJadFRgbwA",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "num",
            "questionTitle": "Age",
            "questionAlias": "age"
          },
          {
            "text": "Reading",
            "questionId": "dZ8lm42uJUxsN0NOn23n",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "mcq",
            "questionTitle": "Hobbies",
            "questionAlias": "hobbies"
          },
          {
            "text": "14/02/2019",
            "date": "2019-02-14",
            "questionId": "RyRm2ASlei",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "dte",
            "questionTitle": "Date of birth",
            "questionAlias": "dob"
          },
          {
            "text": "01:48 PM",
            "time": "13:48",
            "questionId": "rktjrf277g",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "tme",
            "questionTitle": "Time",
            "questionAlias": "time"
          },
          {
            "questionId": "7srg0StYYB",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "loc",
            "location": {
              "coordinates": [
                {
                  "latitude": 28.5162697,
                  "longitude": 77.1979532,
                  "accuracy": 22.426
                }
              ],
              "type": "point"
            },
            "questionTitle": "Location",
            "questionAlias": "location"
          },
          {
            "questionId": "XjW2qlIDRf",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "img",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Image",
            "questionAlias": "image"
          },
          {
            "questionId": "bExN3DDDra",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "sig",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Signature",
            "questionAlias": "signature"
          },
          {
            "text": "IN(+91)-9876543210",
            "phone": "+919876543210",
            "questionId": "lXrfUApTsA",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "phn",
            "questionTitle": "Phone",
            "questionAlias": "phone"
          },
          {
            "questionId": "Cj5Ld8QoJQ",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "aud",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Audio",
            "questionAlias": "audio"
          },
          {
            "text": "Extremely Satisfied",
            "questionId": "RWraLHQHku9zFT7AbeLV",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "fdb",
            "questionTitle": "Likert",
            "questionAlias": "likert"
          },
          {
            "text": "7",
            "number": 7,
            "questionId": "6x5gmiGyHxMyJw7xgkgf",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "sca",
            "questionTitle": "Scale",
            "questionAlias": "scale"
          },
          {
            "text": "5",
            "number": 5,
            "questionId": "VIMtPnhMFOdKEAJbDRvA",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "rat",
            "questionTitle": "Rating",
            "questionAlias": "rating"
          },
          {
            "questionId": "eBjkRMoSjx1HRBFe1mIX",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "geo",
            "location": {
              "coordinates": [
                {
                  "latitude": 28.51628,
                  "longitude": 77.197955,
                  "accuracy": 16.1
                }
              ],
              "type": "point"
            },
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Image Geotag",
            "questionAlias": "image_geotag"
          },
          {
            "questionId": "OnHAmsGjkj8RDJLnKVHz",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "file",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "File Upload",
            "questionAlias": "file"
          },
          {
            "text": "705632441947",
            "questionId": "EHdIi42CAG",
            "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
            "questionTypeCode": "bar",
            "questionTitle": "Barcode",
            "questionAlias": "barcode"
          }
        ],
        "client": "android",
        "formId": "CUD56GdkQM",
        "responseId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
        "responseFamilyId": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
        "_created_at": "2019-02-14T08:20:53.172000Z",
        "_updated_at": "2019-02-14T08:20:53.172000Z",
        "_etag": "e761bd02b6fef8b12f6031c760e7a617a54ce079",
        "_links": {
          "self": {
            "title": "Response",
            "href": "responses/3Ac0KTDaMt0ekIcwxNjM"
          }
        },
        "id": "5b7685a7-a443-4a92-ac6c-5336cb851a1d",
        "createdBy": {
          "username": "919876543210",
          "phone": "+919876543210",
          "fullName": "john Sarva"
        },
        "formTitle": "All Questions"
      },
      {
        "answers": [
          {
            "text": "john",
            "questionId": "5K6D6rtUtF",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "txt",
            "questionTitle": "Name",
            "questionAlias": "name"
          },
          {
            "text": "Male",
            "questionId": "vUEexXhWNS",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "mcq",
            "questionTitle": "Gender",
            "questionAlias": "gender"
          },
          {
            "text": "25",
            "number": 25,
            "questionId": "WJadFRgbwA",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "num",
            "questionTitle": "Age",
            "questionAlias": "age"
          },
          {
            "text": "Sports, Hiking",
            "questionId": "dZ8lm42uJUxsN0NOn23n",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "mcq",
            "questionTitle": "Hobbies",
            "questionAlias": "hobbies"
          },
          {
            "text": "24/12/2018",
            "date": "2018-12-24",
            "questionId": "RyRm2ASlei",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "dte",
            "questionTitle": "Date of birth",
            "questionAlias": "dob"
          },
          {
            "text": "11:11 PM",
            "time": "23:11",
            "questionId": "rktjrf277g",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "tme",
            "questionTitle": "Time",
            "questionAlias": "time"
          },
          {
            "questionId": "7srg0StYYB",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "loc",
            "location": {
              "coordinates": [
                {
                  "latitude": 28.5163167,
                  "longitude": 77.1979675,
                  "accuracy": 23.609
                }
              ],
              "type": "point"
            },
            "questionTitle": "Location",
            "questionAlias": "location"
          },
          {
            "questionId": "XjW2qlIDRf",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "img",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Image",
            "questionAlias": "image"
          },
          {
            "text": "note",
            "questionId": "dyhi1I24WD",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "not",
            "questionTitle": "Note",
            "questionAlias": "note"
          },
          {
            "questionId": "bExN3DDDra",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "sig",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Signature",
            "questionAlias": "signature"
          },
          {
            "text": "a@gmail.com",
            "questionId": "LmGvZ7O5dx",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "ema",
            "questionTitle": "Email",
            "questionAlias": "email"
          },
          {
            "text": "IN(+91)-9876543210",
            "phone": "+919876543210",
            "questionId": "lXrfUApTsA",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "phn",
            "questionTitle": "Phone",
            "questionAlias": "phone"
          },
          {
            "text": "705632441947",
            "questionId": "EHdIi42CAG",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "bar",
            "questionTitle": "Barcode",
            "questionAlias": "barcode"
          },
          {
            "questionId": "Cj5Ld8QoJQ",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "aud",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Audio",
            "questionAlias": "audio"
          },
          {
            "text": "Satisfied",
            "questionId": "RWraLHQHku9zFT7AbeLV",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "fdb",
            "questionTitle": "Likert",
            "questionAlias": "likert"
          },
          {
            "text": "6",
            "number": 6,
            "questionId": "6x5gmiGyHxMyJw7xgkgf",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "sca",
            "questionTitle": "Scale",
            "questionAlias": "scale"
          },
          {
            "text": "4",
            "number": 4,
            "questionId": "VIMtPnhMFOdKEAJbDRvA",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "rat",
            "questionTitle": "Rating",
            "questionAlias": "rating"
          },
          {
            "questionId": "eBjkRMoSjx1HRBFe1mIX",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "geo",
            "location": {
              "coordinates": [
                {
                  "latitude": 28.5163142,
                  "longitude": 77.1979698,
                  "accuracy": 23.703
                }
              ],
              "type": "point"
            },
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Image Geotag",
            "questionAlias": "image_geotag"
          },
          {
            "questionId": "OnHAmsGjkj8RDJLnKVHz",
            "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
            "questionTypeCode": "file",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "File Upload",
            "questionAlias": "file"
          }
        ],
        "client": "android",
        "formId": "CUD56GdkQM",
        "responseId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
        "responseFamilyId": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
        "_created_at": "2018-12-24T17:44:03.387000Z",
        "_updated_at": "2018-12-24T17:44:03.387000Z",
        "_etag": "ef220bef688b601e098aa3db7e0555151b3cccd1",
        "_links": {
          "self": {
            "title": "Response",
            "href": "responses/KFjXB2vH1GGmpgtkyLJC"
          }
        },
        "id": "9c89ed3e-b5b1-4d19-8620-a4e21be2106e",
        "createdBy": {
          "username": "919876543210",
          "phone": "+919876543210",
          "fullName": "john Sarva"
        },
        "formTitle": "All Questions"
      },
      {
        "answers": [
          {
            "text": "Yatin",
            "questionId": "5K6D6rtUtF",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "txt",
            "questionTitle": "Name",
            "questionAlias": "name"
          },
          {
            "text": "Male",
            "questionId": "vUEexXhWNS",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "mcq",
            "questionTitle": "Gender",
            "questionAlias": "gender"
          },
          {
            "text": "2",
            "number": 2,
            "questionId": "WJadFRgbwA",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "num",
            "questionTitle": "Age",
            "questionAlias": "age"
          },
          {
            "questionId": "7srg0StYYB",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "loc",
            "location": {
              "coordinates": [
                {
                  "latitude": 28.5162884,
                  "longitude": 77.1979387,
                  "accuracy": 23.31
                }
              ],
              "type": "point"
            },
            "questionTitle": "Location",
            "questionAlias": "location"
          },
          {
            "text": "14/03/2017",
            "date": "2017-03-14",
            "questionId": "RyRm2ASlei",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "dte",
            "questionTitle": "Date of birth",
            "questionAlias": "dob"
          },
          {
            "text": "02:00 PM",
            "time": "14:00",
            "questionId": "rktjrf277g",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "tme",
            "questionTitle": "Time",
            "questionAlias": "time"
          },
          {
            "questionId": "XjW2qlIDRf",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "img",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Image",
            "questionAlias": "image"
          },
          {
            "questionId": "bExN3DDDra",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "sig",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Signature",
            "questionAlias": "signature"
          },
          {
            "text": "test",
            "questionId": "dyhi1I24WD",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "not",
            "questionTitle": "Note",
            "questionAlias": "note"
          },
          {
            "text": "a@b.com",
            "questionId": "LmGvZ7O5dx",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "ema",
            "questionTitle": "Email",
            "questionAlias": "email"
          },
          {
            "text": "IN(+91)-9876543210",
            "questionId": "lXrfUApTsA",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "phn",
            "questionTitle": "Phone",
            "questionAlias": "phone"
          },
          {
            "text": "90162602",
            "questionId": "EHdIi42CAG",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "bar",
            "questionTitle": "Barcode",
            "questionAlias": "barcode"
          },
          {
            "questionId": "Cj5Ld8QoJQ",
            "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
            "questionTypeCode": "aud",
            "media": [
              "https://some-link"
            ],
            "questionTitle": "Audio",
            "questionAlias": "audio"
          }
        ],
        "client": "android",
        "formId": "CUD56GdkQM",
        "responseId": "e3028368-ba05-42f1-814e-fca77976f3db",
        "_created_at": "2017-03-14T08:34:57.229000Z",
        "_updated_at": "2017-03-14T08:34:57.229000Z",
        "_etag": "b77aa5c035134ea12992d46e42347134ac0a9aef",
        "_links": {
          "self": {
            "title": "Response",
            "href": "responses/45aTHDxlxj"
          }
        },
        "id": "e3028368-ba05-42f1-814e-fca77976f3db",
        "createdBy": {},
        "formTitle": "All Questions"
      }
    ],
    "_links": {
      "parent": {
        "title": "home",
        "href": "/"
      },
      "self": {
        "title": "responses",
        "href": "responses?max_results=20&where={\"formId\":\"CUD56GdkQM\"}"
      }
    },
    "_meta": {
      "page": 1,
      "max_results": 20,
      "total": 3,
      "total_pages": 1
    }
  }
        
        return jsonify(message)


api.add_resource(RatingResponse, '/')


# driver function
if __name__ == '__main__':

    app.run(debug=True)
